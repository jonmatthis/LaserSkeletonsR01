import asyncio
from pathlib import Path
from typing import Union

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
load_dotenv()
def create_summary_chain():
    prompt = ChatPromptTemplate.from_template("Summarize the following text: \n {text}")
    model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
    chain = prompt | model
    return chain




async def auto_document(document_root_path: Union[Path, str]):
    # document_tree = DirectoryTreeBuilder.from_path(path=document_root_path)
    # print(document_tree)
    summary_chain = create_summary_chain()

    output_text = ""
    for path in Path(document_root_path).rglob("*"):
        if path.is_file():
            if path.suffix == ".tex":
                file_content = path.read_text()

                text_to_analyze = (f"{str(path)}\n"
                                   f"{file_content}")

                summmary_text =""
                for token in summary_chain.stream({"text":text_to_analyze}):
                    print(token.content, end="", flush=True)
                    summmary_text += token.content

                header_1 = "# " + path.name
                header_2 = f"## Summary \n{summmary_text}"
                output_text += f"{header_1}\n{header_2}\n\n"

    print(output_text)

    with open("document_summary.md", "w", encoding="utf-8") as file:
        file.write(output_text)



if __name__ == "__main__":
    document_root_path = Path(__file__).parent.parent.parent / "document"
    asyncio.run(auto_document(document_root_path=document_root_path))
