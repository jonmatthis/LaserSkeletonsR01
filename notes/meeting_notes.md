[![hackmd-github-sync-badge](https://hackmd.io/MSdlHX3mSw6p6-ETGeP1BQ/badge)](https://hackmd.io/MSdlHX3mSw6p6-ETGeP1BQ)
overleaf link - https://www.overleaf.com/project/648a8124eb9fb7e98477ad0e
Jon's K99/R00 proposal - https://www.dropbox.com/s/x8vmci8o73lce49/Matthis_K99_July2017_Full%20Proposal%20v2.pdf?dl=0
Google link - https://docs.google.com/document/d/1WBKwk5Bw2Htwp9L7vK6bXMou-sFu_T3C-OYm3GT3TIg/edit



# Kate and Jon  - Laser Skelly R01

## 2023-08-29: Dump of Kate's Approach outline of Aim 1

- General Methods:  

Data collection with mobile eyetracker (Pupil Labs) and Rokoko body motion suit. n=50

Multiple types of terrain.  Must haves: pavement (smooth flat beautiful), medium, very rocky
We want double-pass experiments within each condition as well… Thus 6 out-and-back passes.

Divided attention tasks. Repeat walking with a phone game and/or conversation partner who walks behind them … alongside them?

Screenings (Talk to OD students).
Acuities (monocular, binocular)
Stereo-vision (asteroids?)
Y balance test (dynamic balance)


- Research Design: 

The resulting data will provide the opportunity to answer several questions about visual perception, gaze, gait, the environment, and the coordination of these during walking.  

- i. How do people allocate gaze during foothold finding?  What is the planning horizon? 
    - Allocation to footholds, non-foothold search locations, [divided attention: task fixations that are on the conversation partner or directed at their phone]
    - Search fixations?  turns…
    - This provides a window into the planning horizon (Kuo predicts it is 5-8 steps ahead).  We suspect that 5 is more correct in these natural environments.  Based on previous work… limitations of sight.  
- ii. How do people modulate their gaze relative to their speed of travel? 
    - Measure look ahead distance and time
    - Previous work shows that we modulate our look ahead distance while keeping look ahead time constant.
    - There is a shift with knocked down binocular vision
- iii. How is gaze allocation modulated by moment-to-moment instability?
    - gaze allocation? Look-ahead distance? Look-ahead time? Speed (definitely yes)?
    - Measurement of instability: deviation from idealized inverted pendulum based on body measurements in and walking on flat pavement
    - How does it impact the next 2-5 fixations? Conditioned on speed.
- iv. What makes a “good” foothold? 	
    - Grade of foothold (Karl analysis)
    - Texture analysis of pixel intensities and depth values

- v. What is the natural variability in toe clearance? This might seem strange but
    - Thought to be  a sign of increased caution, potentially an inability to be precise either because of visual or motor noise.  We expect to see an increase in toe clearance with changes in terrain complexity. 
    - Increases in toe clearance are often observed in visual impairment and aging.  
    
- vi-x. How does divided attention impact the ?  Divided Attention: Repeat analysis A-E for the divided attention conditions. 
    - i. Allocation to footholds, non-foothold search locations, [divided attention: task fixations that are on the conversation partner or directed at their phone]
    - Understanding these differences is critical, because walking in daily life is more likely to occur under divided attention.  
    - People will spend less time attending to footholds, allocating some fixations to the task.  We can examine this attentional tradeoff by comparing how gaze allocation changes across two tasks that have different visual information needs.
    - Are there measurable changes to toe clearance?  Perhaps not.  If there was… more caution might be expected in cases when the body is engaged in two tasks.
    - Do we see more instability with attention engaged elsewhere?  Or does the body do this in such an automatic way that we don’t?
    - Footholds… Does the choice of them become more careless in quantifiable ways?



## some stuff without a date
 - Technical deliverables
     - Ability for others to: 
         - get outdoor laser skellys (via Rokoko + Pupil or something)
         - get lab laser skellys (i.e. Unity based ARGP experiments)
         - Analyze data (either their OWN or our datasets)
     - Share data online repo or something (i.e. we upload our laser skellys for others to use, and also they can add their own data)
         - with shared/generic data processing pipelines

## 2023-06-23
- Got/getting berkeley etc data from UT Crew
    - can get `all_walks.mat` data and basic mesh data easily, Stern mailing hard drives to Kate
    - Putting a sample subject in the NAS under "Bonnen_LaserSkeletons" or something

## 2023-06-15

- evaluated skelly-lasers
- Updates
    - Jon/Michael are analyzing data on augmented ground plane. using a skelly-lasers that Trent created.
    - target footholds (no distractors)  Manipulate the density of targets.  How many places are there to put your feet?
    - 5 levels of density, 5 configurations of terrain that get repeated 5 times.

## 2023-06-14
kate and the golemgardenbot have a chat about user stories and this falls out...

1. User
   - Graduate student in the lab

2. Data Types
   a. Eye movement data
       Collected with a Pupil Labs eye tracker
   b. Body motion data
   Collected using Free mocap, Rococo suit, or Motion Shadow suit

3. User Needs
   - integrate eye movement / head-mounted video / body motion data
   - output integrated data numerically

Now, let's transform this outline into a user story with acceptance criteria:

User Story:
"As a graduate student in the lab, I want integrate eye movement, and body motion data, so that I can connect my eye measurements to my body measurements."

Acceptance Criteria:
- The system can import eye movement data from a Pupil Labs eye tracker.
- The system can import body motion data from Free mocap, Rococo suit, or Motion Shadow suit.
- The user can visualize the data in a clear and informative manner.
- The user can obtain a skelly-laser data object for further analysis.


## 2023-06-07
### Agenda
- sparse/dense augmented ground plane info
- [Kate] skellylasers
    - structure -- Kate's not sure how to integrate into the package skeleton.  What are the names of all the things I'm implementing so I can ask Chatgpt?
        - tests
        - github actions
        - should there be a gui (?) 
        - ??
    - refactor
        - functioning code is in pupil_labs_stuff

### Notes
- sparse/dense data --> Jon has a single subject's data.  They have post-processed to the point of skeletons/lasers.  Need to splice into conditions.
- Skelly-lasers: Start with a user story - what do you want to do? I am a vision scientist.  I want to make laser skeletons.  What am I going to do next.
    - architecture
        - structure of code.
    - entry point (gui instead of random file)

### Homework
 - Jon
     - Get details about what the ARGP pilot data actually is (i.e. conditions, num reps, current status, etc)
- Kate
    - Write down a user story for skelly lasers.  Don't think about how it should be implemented. 
    - Send to jon
    - use Chat GPT to help you :) 


## 2023-06-01

### Aim 1 - Look at outdoor dataset for stuff (Quasi observational, ecologically valid)
- Scientific stuff
    - Basic analysis of gaze/foothold and gaze timing.  How people modulate gaze to support postural stability during walking
    - moment to moment instability --> eye movements
    - Infer motor planning from gaze location / patterns
    - Pilot data will be Berkely Dataset
- Deliverable dataset 
    - 20-30 more folkums
    - Some sort of 'legit' dataset hosted online

### Aim 2 - Indoor controlled experiments
- Pilot - ARGP data (Trent/Michaels data)
    - We need to see what the current sparse/dense knob does to behavior.  This will help us to understand what some blind hypotheses can be for this section. 

- Deliverable: 
    - controlled exps to test hypotheses genreated  in Aim 1

### Aim 3 - Some kinda distracter biz
- looking at phone / talking to a person (?)
- When we have limited gaze resources where do we use them?  This is what happens in real life.
- How much do people actually need to look at the ground?
- Does this change motor planning patterns?


Global Deliverables:
- Science stuff
    - How lasers?
- Tech stuff
    - Easy to get lasers
        - Methods to collect this kind of stuff easier
    - Easy to share lasers
        - Publicly hosted datasets
    - Easy to analyze lasers
        - Professional grade pre/post processing and analysis pipelines. 
        
        
- Homework - build ingestion piplines for different datasets into common format for analysis


## Timeline

- R01 Deadline: October 5th
- [Kate] Set up regular writing sessions
- [Kate] Meet with Michael/Jon about sparse/dense indoor walking data. (first meeting before June 15)
- Specific aims should be read/sent to (July 15th)
    - Mary Hayhoe
    - Konrad Kording
    - Larry Cormack
    - Kate's tenure committee: Nicholas Port, Rowan Candy, Josh Brown
    - Alex Huk (he's good at the game, even if we're not always excited...)
- 

