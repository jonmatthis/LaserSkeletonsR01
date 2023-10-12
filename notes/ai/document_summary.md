+++++++++++++++++++++++++++++++++++

FILE_PATH - C:\Users\jonma\github_repos\jonmatthis\LaserSkeletonsR01\document\research_strategy\main_research_strategy.tex
STATUS - In progress

## A. Significance
### [subsection name]
#### [subsubsection name]

## B. Innovation

## C. Approach
### [subsection name]

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - C:\Users\jonma\github_repos\jonmatthis\LaserSkeletonsR01\document\research_strategy\sections\innovation.tex
STATUS - In progress

## Integrated visuomotor datasets from humans walking in real-world environments
### New technologies: photogrammetry methods for improved accuracy of body/gaze calibration
### Dataset one order of magnitude larger than existing datasets
### Re-usable data collection pipelines

## Augmented reality ground plane
### Body + eye movement contingent
### Complementary to outdoor data collection
### Generation of complex scenes for precise control
### Allows isolation/testing of real-world observations

Notes:
- Strengths
  - Integration of new technologies for improved accuracy and larger datasets
  - Use of augmented reality for precise control and isolation of observations
- Weaknesses
  - No mention of specific research questions or hypotheses

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - C:\Users\jonma\github_repos\jonmatthis\LaserSkeletonsR01\document\research_strategy\sections\significance.tex
STATUS - In progress

## A.1 Humans have a robust visuomotor control system that supports walking in complex environments
### Closed loop system:
- Biomechanics of walking constrains visual behavior
- Looking 2-5 steps ahead
- Incorporating upcoming obstacles to maximize energetic efficiency

### Lack of model human walkers and appropriate datasets
- Most datasets aren't egocentric
- Datasets with complete body pose information are needed to understand the relationship between visual perception and action
- Large datasets with eye movements and world content are available, but datasets with stored actions are needed

## A.2 Visual search patterns are efficient and task-dependent
- Visual search patterns are fixation-efficient and eye movements are made to maximize the probability of finding the target
- Visual search is highly task-dependent and eye movements are made to serve the current task demands and reduce uncertainty

## A.3 [No content provided]

## A.4 Summary of significance
- The proposal is supported by past research showing the general patterns of visuomotor control
- The proposal aims to leverage improved processes for collecting integrated visuomotor datasets and develop laboratory protocols to enhance understanding of the visuo-locomotor system
- The gap in knowledge restricts understanding of how the visuo-locomotor system is affected by aging and disease

Notes:
- Strengths:
  - Focus on the relationship between visual perception and action in the visuo-locomotor system
  - Utilization of improved processes for data collection
- Weaknesses:
  - Lack of model human walkers and appropriate datasets
  - Limited understanding of how the visuo-locomotor system is affected by aging and disease

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - C:\Users\jonma\github_repos\jonmatthis\LaserSkeletonsR01\document\research_strategy\sections\approach\main_approach.tex
STATUS - In progress

## Aim 1: Visually-guided walking in complex terrains
### Subsection: 
#### Subsubsection: 

## Aim 2 - ARGP Stuff
### Subsection: 
#### Subsubsection: 

Notes:
- Strengths
    - None provided
- Weaknesses
    - None provided

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - C:\Users\jonma\github_repos\jonmatthis\LaserSkeletonsR01\document\research_strategy\sections\approach\aim_1\main_aim_1.tex
STATUS - In progress

## Rationale
The aim of this section is to describe and model visual perception, visual selection (gaze), and biomechanics (gait) in the context of walking in real-world environments. The goal is to provide an integrated account of the sensorimotor processing underlying visually-guided walking.

### Specific Fixation Strategies
The researchers will measure and model the fixation strategies used by walkers during foothold finding and evaluate how these strategies are influenced by biomechanical constraints. They aim to determine which visual and biomechanical information is most predictive of the location of the next footfall and/or gaze location.

### Divided Attention Conditions
The researchers will investigate the tradeoffs that walkers make to maintain stability and find footholds while engaging in other tasks. They will examine how walkers modify their fixation patterns when splitting their attention between tasks and whether there are stereotyped fixation sequences.

## General Methods
Participants will be recruited and screened to include healthy young adults with normal or corrected-to-normal vision and typically functioning motor systems. Data collection will involve measuring visual acuities, stereo-vision, and conducting a Y balance test. The researchers will recruit a diverse set of participants from various locations.

Data collection will be conducted from 75 participants over the first 2-3 years of the grant period. The dataset size is relatively large for this type of data collection and will enable the researchers to establish estimates of individual variability and support effective modeling efforts.

The methods for data collection rely on a mobile eye tracker, a body motion suit, and a lightweight computer. A 9-point VOR eye tracking calibration procedure is used to calibrate the eye tracker and place the body motion data in the same reference frame as the gaze data. A photogrammetry pipeline provides a reconstruction of the environment and the location of the head-mounted camera.

Participants will perform walking bouts in different terrains and conditions, including single task, divided attention - talking, and divided attention - phone. Data analysis will be performed using custom open-source processing pipelines written in Python.

## Technical Deliverables
The grant aims to lower the barrier to the collection and analysis of integrated visuomotor datasets in real-world environments. The researchers will provide detailed open-source documentation for the hardware integration and data collection. They will also develop data processing pipelines and share them as open-source packages on Github. The integrated visuomotor dataset will be made available as a data repository on Zenodo.

## Research Design
The resulting data will be used to answer various questions about visual perception, gaze, gait, the environment, and their coordination during walking. The researchers will investigate gaze allocation during foothold finding, the modulation of gaze allocation by step-to-step gait efficiency, the factors that make a "good" foothold, individual variability in ground clearance, and the impact of divided attention on visuomotor control of walking.

## Experimental Concerns
The researchers address concerns about the difficulty of the study by referring to previous published studies that they were authors in. They also plan to complete the walking bouts in a randomized order twice to account for learning effects.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - C:\Users\jonma\github_repos\jonmatthis\LaserSkeletonsR01\document\research_strategy\sections\approach\aim_2\main_aim_2.tex
STATUS - In progress
## Rationale:
The need for laboratory-precision measurements is discussed, highlighting the importance of accuracy, controllable terrain, and hypothesis testing.

## General Methods: The Augmented Reality Ground-Plane (ARGP):
The ARGP is described as a projector-based, indoor walking path that allows for real-time interactive display of terrain and auditory feedback. References to previous studies using the ARGP are provided.

### General Design:
The design of the experiments is explained, including the recruitment of participants and the completion of "free walking" trials to establish a baseline measurement of preferred gait cycle (PGC). Simple metrics such as walking speed, step length, and step width are mentioned, as well as more complex measures related to center of mass (COM) and base of support (BOS). The relationship between gaze and gait is also discussed.

## Gaze/Gait relationship in terrain of various foothold density:
Three experiments or conditions are outlined. The first involves manipulating foothold density, the second adds distractors to the terrain, and the third examines gaze and foothold patterns to create contrived paths with dead-zones and funnels. The goal is to analyze gaze and gait patterns in these conditions and explore the planning of straight-ahead paths versus curved paths.

# Analyses:
The hypothesis to test is whether fixation patterns are driven by biomechanics or vision, and the integration of gaze and gait is discussed. Baseline modeling is proposed, including the analysis of gaze and gait integration, basic statistics, body-centered measures (such as the LIP model and preferred gait cycle), and retinal-centered measures (such as retinal optic flow and visual search).

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - C:\Users\jonma\github_repos\jonmatthis\LaserSkeletonsR01\document\specific_aims\main_specific_aims.tex
STATUS - In progress

## Specific Aims
### SA1: Information gathering and motor planning during full-body movement through real-world environments
- Lack of normative baseline data on how individuals use vision to guide walking in complex environments
- Collect integrated visuomotor dataset in 50 adults with typical vision and motor function
- Analyze motor planning strategies, gaze behavior, and coordination of gaze and gait during visually-guided walking
- Technical deliverables: comprehensive visuomotor dataset, open-source documentation of hardware infrastructure, open-source software processing pipeline

### SA2: Testing the spatial and temporal dynamics of visual information gathering and motor planning
- Develop augmented reality ground plane for presenting walking paths
- Manipulate availability of visual information based on body position and gaze location
- Identify critical information for foothold selection during walking
- Technical deliverables: open-source hardware specifications for augmented reality ground-plane, open-source software processing pipeline

### SA3: Impact of Divided on Attention on the visuomotor control of walking
- Measure impact of divided attention on coordination of gaze and gait during full-body movement
- Participants will engage in divided attention tasks while walking
- Insight into allocation of visual information gathering and motor planning resources during multitasking
- Technical deliverables: divided attention extension to comprehensive visuomotor dataset

Notes:
- Strengths
  - Comprehensive approach to understanding sensorimotor processes involved in visually-guided walking
  - Integration of real-world behavior and laboratory measurements
  - Unique position with developed data collection techniques and interdisciplinary expertise
- Weaknesses
  - Lack of normative baseline data and integrated visuomotor datasets
  - Relatively small sample size of 50 adults with typical vision and motor function

-----------------------------------

=============================================================

=============================================================

___ 
 > Global Summary 
  Here is a summary of the key points and proposed aims from the background information provided:

The overarching goal is to develop an integrated model of the visuomotor processes that support movement through real-world environments. This will provide a detailed account of the visual information gathering and cognitive/motor planning processes involved in walking, taking into account divided attention. 

The aims are:

1. Collect an integrated visuomotor dataset (eye tracking, body motion, environment) of 50 adults walking in real-world environments. Analyze motor planning strategies, gaze behavior changes with gait instability, and identify advantageous gaze patterns. Deliverables: comprehensive dataset, data collection/processing infrastructure.

2. Develop laboratory protocols using an augmented reality ground plane to systematically control visual information during walking. Test hypotheses about motor planning and gaze-gait coordination derived from real-world observations. Deliverables: AR ground plane hardware/software, integrated data processing.

3. Examine the impact of divided attention on gaze-gait coordination by having participants walk while engaged in secondary tasks. Deliverable: Extension of comprehensive dataset to include divided attention. 

The proposed research will provide critical foundational data and models describing the integration of visual and motor processes

```

🌱
├── bibliography/
│   ├── bibliography.bib/
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: bibliography.bib
│   │       ├── file_type: .bib
│   │       ├── file_stats
│   │       │   ├── bytes: 89083
│   │       │   ├── last_modified_utc: 1697141083.3380926
│   │       │   ├── last_accessed_utc: 1697141434.6156538
│   │       │   └── created_utc: 1697130015.5711725
│   │       └── content: 
│   │           @online{noauthor_perception_nodate,
│   │                   title = {Perception of another person’s maximum 
│   │           reach-with-jum
│   │           ...
│   │           y: General},
│   │                   author = {Cutting, James E and Springer, Ken},
│   │                   date = {1992},
│   │                   langid = {english},
│   │           }
│   │           
│   └── main_bibliography.tex/
│       ├── type: file
│       └── content
│           ├── file_name: main_bibliography.tex
│           ├── file_type: .tex
│           ├── file_stats
│           │   ├── bytes: 118
│           │   ├── last_modified_utc: 1697141083.3390908
│           │   ├── last_accessed_utc: 1697141437.257229
│           │   └── created_utc: 1697130015.5721917
│           └── content: \bibliographystyle{plain} % We choose the "plain" 
│               reference style
│               \bibliography{document/bibliography/bibliography}
│               
├── boilerplate/
│   ├── inclusion_of_women_and_minorities.tex/
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: inclusion_of_women_and_minorities.tex
│   │       ├── file_type: .tex
│   │       ├── file_stats
│   │       │   ├── bytes: 353
│   │       │   ├── last_modified_utc: 1697130015.5721917
│   │       │   ├── last_accessed_utc: 1697140016.443652
│   │       │   └── created_utc: 1697130015.5721917
│   │       └── content: \section*{7. Inclusion of Women and Minorities}
│   │           
│   │           Refer to Part II, Supplemental Instructions for Pre
│   │           ...
│   │           olved?" on the R\&R Other Project Information form and the 
│   │           research does not fall under Exemption 4.
│   ├── main_boilerplate.tex/
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: main_boilerplate.tex
│   │       ├── file_type: .tex
│   │       ├── file_stats
│   │       │   ├── bytes: 9901
│   │       │   ├── last_modified_utc: 1697130015.5721917
│   │       │   ├── last_accessed_utc: 1697140016.443652
│   │       │   └── created_utc: 1697130015.5721917
│   │       └── content: 
│   │           %--------------------------------------------------------------
│   │           --------------------------
│   │           %       INCLUSIO
│   │           ...
│   │           sociation Studies, NIH Guide NOT-OD-07-088, and 
│   │           http://grants.nih.gov/grants/gwas/.
│   │           \end{enumerate}
│   │           
│   └── protection_of_human_subjects.tex/
│       ├── type: file
│       └── content
│           ├── file_name: protection_of_human_subjects.tex
│           ├── file_type: .tex
│           ├── file_stats
│           │   ├── bytes: 637
│           │   ├── last_modified_utc: 1697130015.5731792
│           │   ├── last_accessed_utc: 1697140016.443652
│           │   └── created_utc: 1697130015.5731792
│           └── content: \section*{6. Protection of Human Subjects}
│               
│               Refer to Part II, Supplemental Instructions for Preparin
│               ...
│               se the protection of human subjects section to circumvent the 
│               page limits of the Research Strategy.
│               
├── figures/
│   ├── Figure-1-outdoor-walking.pdf/
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: Figure-1-outdoor-walking.pdf
│   │       ├── file_type: .pdf
│   │       ├── file_stats
│   │       │   ├── bytes: 41252143
│   │       │   ├── last_modified_utc: 1697130015.7413497
│   │       │   ├── last_accessed_utc: 1697137936.9683385
│   │       │   └── created_utc: 1697130015.7303498
│   │       └── content: <content could not be loaded>
│   ├── Figure-2-outdoor-walking-analyses.pdf/
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: Figure-2-outdoor-walking-analyses.pdf
│   │       ├── file_type: .pdf
│   │       ├── file_stats
│   │       │   ├── bytes: 1099017
│   │       │   ├── last_modified_utc: 1697130015.7473416
│   │       │   ├── last_accessed_utc: 1697137936.9793322
│   │       │   └── created_utc: 1697130015.7463493
│   │       └── content: <content could not be loaded>
│   └── Figure-3-walker-diagram-experiment-landolt-Cs.pdf/
│       ├── type: file
│       └── content
│           ├── file_name: Figure-3-walker-diagram-experiment-landolt-Cs.pdf
│           ├── file_type: .pdf
│           ├── file_stats
│           │   ├── bytes: 1776353
│           │   ├── last_modified_utc: 1697130015.75535
│           │   ├── last_accessed_utc: 1697137936.9813313
│           │   └── created_utc: 1697130015.7543492
│           └── content: <content could not be loaded>
├── header/
│   └── main_header.tex/
│       ├── type: file
│       └── content
│           ├── file_name: main_header.tex
│           ├── file_type: .tex
│           ├── file_stats
│           │   ├── bytes: 2243
│           │   ├── last_modified_utc: 1697130015.7563505
│           │   ├── last_accessed_utc: 1697140016.4416533
│           │   └── created_utc: 1697130015.7563505
│           └── content: %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
│               % NIH Grant Proposal for the Specific Aims and Research Pl
│               ...
│               rtran} % Specifies custom hyphenation points for words or words
│               that shouldn't be hyphenated at all
│               
├── research_strategy/
│   ├── main_research_strategy.tex/
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: main_research_strategy.tex
│   │       ├── file_type: .tex
│   │       ├── file_stats
│   │       │   ├── bytes: 905
│   │       │   ├── last_modified_utc: 1697130015.7573419
│   │       │   ├── last_accessed_utc: 1697141518.9942012
│   │       │   └── created_utc: 1697130015.7573419
│   │       └── content: \newpage
│   │           \title{Research Strategy}
│   │           
│   │           %--------------------------------------------------------------
│   │           -
│   │           ...
│   │           --------
│   │           \section*{C. Approach}
│   │           \input{document/research_strategy/sections/approach/main_approa
│   │           ch}
│   │           
│   │           
│   └── sections/
│       ├── innovation.tex/
│       │   ├── type: file
│       │   └── content
│       │       ├── file_name: innovation.tex
│       │       ├── file_type: .tex
│       │       ├── file_stats
│       │       │   ├── bytes: 2323
│       │       │   ├── last_modified_utc: 1697130015.7583413
│       │       │   ├── last_accessed_utc: 1697141518.9942012
│       │       │   └── created_utc: 1697130015.7583413
│       │       └── content: \begin{itemize}
│       │           
│       │           
│       │           \item
│       │             Integrated visuomotor datasets from humans walking in 
│       │           real-world
│       │             environ
│       │           ...
│       │           ufficient to understand the
│       │             influence of biomechanical constraint in visual search.
│       │           \end{itemize}
│       │           
│       ├── significance.tex/
│       │   ├── type: file
│       │   └── content
│       │       ├── file_name: significance.tex
│       │       ├── file_type: .tex
│       │       ├── file_stats
│       │       │   ├── bytes: 4226
│       │       │   ├── last_modified_utc: 1697141083.3400915
│       │       │   ├── last_accessed_utc: 1697141518.9942012
│       │       │   └── created_utc: 1697130015.7593412
│       │       └── content: 
│       │           \textbf{A.1 Humans have a robust visuomotor control system 
│       │           that supports walking in complex environ
│       │           ...
│       │           df}
│       │           \caption{\textbf{Outdoor measurements of the 
│       │           visuo-locomotor system.} A. ?? B. ??}
│       │           \end{figure}
│       │           
│       └── approach/
│           ├── main_approach.tex/
│           │   ├── type: file
│           │   └── content
│           │       ├── file_name: main_approach.tex
│           │       ├── file_type: .tex
│           │       ├── file_stats
│           │       │   ├── bytes: 632
│           │       │   ├── last_modified_utc: 1697130015.7583413
│           │       │   ├── last_accessed_utc: 1697141518.995193
│           │       │   └── created_utc: 1697130015.7583413
│           │       └── content: 
│           │           %------------------------------------------------------
│           │           ----------------------------------
│           │           %       Aim 1
│           │           %
│           │           ...
│           │           ubsection{Aim 2 - ARGP Stuff}
│           │           \input{document/research_strategy/sections/approach/aim
│           │           _2/main_aim_2}
│           │           
│           ├── _schema.md/
│           │   ├── type: file
│           │   └── content
│           │       ├── file_name: _schema.md
│           │       ├── file_type: .md
│           │       ├── file_stats
│           │       │   ├── bytes: 135
│           │       │   ├── last_modified_utc: 1697130015.7573419
│           │       │   ├── last_accessed_utc: 1697139832.9335728
│           │       │   └── created_utc: 1697130015.7573419
│           │       └── content: # Aim title
│           │           
│           │           ## Rationale
│           │           
│           │           ## General Methods
│           │           
│           │           ## Technical Deliverables
│           │           
│           │           ## Research Design
│           │           - Question 1
│           │           - Question 2
│           │           - etc
│           ├── aim_1/
│           │   └── main_aim_1.tex/
│           │       ├── type: file
│           │       └── content
│           │           ├── file_name: main_aim_1.tex
│           │           ├── file_type: .tex
│           │           ├── file_stats
│           │           │   ├── bytes: 18612
│           │           │   ├── last_modified_utc: 1697138074.5564046
│           │           │   ├── last_accessed_utc: 1697141518.995193
│           │           │   └── created_utc: 1697130015.7573419
│           │           └── content: 
│           │               
│           │               \textbf{\underline{Rationale:}}  The main goal of 
│           │               this aim is to is to jointly describe and model 
│           │               ...
│           │               e of learning effects across sessions we can
│           │                 consider collecting data at two sites.
│           │               \end{itemize}
│           │               
│           └── aim_2/
│               └── main_aim_2.tex/
│                   ├── type: file
│                   └── content
│                       ├── file_name: main_aim_2.tex
│                       ├── file_type: .tex
│                       ├── file_stats
│                       │   ├── bytes: 7451
│                       │   ├── last_modified_utc: 1697141229.34116
│                       │   ├── last_accessed_utc: 1697141518.995193
│                       │   └── created_utc: 1697130015.7583413
│                       └── content: AUGMENTED REALITY GROUND PLANE - 
│                           Laboratory-precision measurements of
│                           visually-guided walking
│                           
│                           \sect
│                           ...
│                           ihood of finding a target in a given area of the 
│                           visual field (using RV1 model)
│                           
│                           
│                           
│                           % \end{document}
│                           
└── specific_aims/
    └── main_specific_aims.tex/
        ├── type: file
        └── content
            ├── file_name: main_specific_aims.tex
            ├── file_type: .tex
            ├── file_stats
            │   ├── bytes: 12213
            │   ├── last_modified_utc: 1697130015.7593412
            │   ├── last_accessed_utc: 1697141518.995193
            │   └── created_utc: 1697130015.7593412
            └── content: 
                \section*{Specific Aims}
                
                % Following this sort of format: 
                https://www.biosciencewriters.com/NIH-Gr
                ...
                low us to move the joint study of walking and eye movement from
                the laboratory into the real world.
                


```

