# General Design/Data stuff

### Data types

#### [Lasers] Optical (eye tracker stuff)
- Where are the eyes pointing? 
  - measures moment-to-moment cognitive decision maing
  - neurophysiological ability to fixate/VOR good
  - where in the world are you choosing to pull a sample from (vs anywhere else you could've looked)
    - ...and what does that say about the internal optimizations/control strategies involved inmoving your floppy meat puppet round the world? 
#### [Skeletons] Kinematic (mocap stuff)
- Full body center of mass
- Biomechanics stuff, measures the 'output'
- Relevant to musculoskeletal/movement/motor disorders
#### [Laser Skeletons] Integration!
- attach the lasers to the skeleton
- Now you can say things about the whole perception/action cycle (Warren 2006)
#### Massed data vs 'per-action' data
- [EASIER] Massed data is BIG stats of whole condition lumped together
- what are the stats of Bx in this conditon?
- [HARDer] Per-action data is stats of each individual action chunk (e.g. each step, or each fixation)
- what was going on when the subject did that specific thing? (e.g. what was the fixation duration when the subject took that step?)


## Design (Within-subject functional self-normalization)
- All studies will be within-subjects designs, with each participant completing all conditions.    
    - We don't need to worry about inter-subject variability (which would be quite high b/c people are complicated) - its like 'auto-normalization' or ' functional self-normalization' or something
        - We should cite some "individual differences" papers here, e.g. maybe some Monica Daley stuff?


- Participants will complete "free walking" trials wherein they'll walk from Start to End a `number_of_trials_per_condition` time at a 'comfortable walking pace'
    - We will then use data from these conditions as a 'baseline' measurement of 'preferred gait cycle' (PGC) for each participant, which is presumed to be the 'optimal' configuration on whatever internal value system folks use (Donelan/Selinger 2006ish)

- Also a perscribed regularized ground fixation task for validating intergation
- VOR calibration task 


### Planned Comparisons
- Examine how these characteristics change as participants walk through different conditions, interpretting changes from PGC as trade-offs occurring in service of some other point of value.

- Use devitions from PGC as a way to target specific sections of behavior for deeper analysis (see 'massed data' vs 'per-action data' below)

- In Lab study - we can fiddle with the knobs to figure out what the 'trade-offs' are w.r.t. gait parameters and environmental/task constraints.
    - then compare that to Outdoor data in order to characterize the 'challenge/trade-off/etc profile' of the outdoor terrain in order to figure out what makes a given terrain 'challenging' and how those challenges are adapted to at the musculoskeletal level (applications for aging - assist in characterizing multi-dimensional functional declines. i.e. perceptual vs cognitive vs motor vs musculoskeletal, etc)


## Analyses

- Hypothesis to test: Are fixation patterns driven by biomechanics ("I wish I could step there, so I will look there and see if there's a foothold available) or vision ("Peripheral cues suggest there's a foothold there, so let me fixate it to see if its something I want to put my foot on it")

    - obviously its gonna be gonna be a combo of both, but how/when do they trade off? 
  
    - e.g. Fig 2 of Trent's f32

- Baseline modelling

  - Gaze/gait integration:
  
    - how hard are peeps fixating footholds in the different conditions?
    
        - e.g. figs 3, 4,5, in Matthis Current Bio

  - Basic stats:
  
    - look ahead distance vs timing (prediction - timing is constant-ish in 1.5-2sec range, look ahead distance varies with terrain/walking speed)
    
    - deviations from PGC (prediction - deviations are larger in sparse terrain, and in distractor conditions, e.g. Fig 2 Matthis Current Bio)
    
    - speed fluctuations (prediction - speed fluctuations are larger in sparse terrain, and in distractor conditions, e.g. 'energy recovery' in matthis 2013 (proc roy soc B), figs 4, 5)
    
    - fixation duration (no real predictions, but a stat to compare/diffrentiate between conditions)
  
  - Body-centered:
  
      - LIP model (COM trajectory relative to planted foot, e.g. Koolen/Rebula/Pratt paper, Matthis Fajen 2013,14, etc)
      
      - Prefered gait cycle (literally just step length, width, timing, e.g. Donelan stuff, e.g. Fig 2 Matthis current bio)

  
  - Retinal-centered:
  
      - Retinal optic flow div/curl relative to eyeball trajecotories (e.g. Matthis et al 2023)
      
        - look for increased stabilization in distractor vs no-distractor conditions (e.g. exp 1/2), e.g. 'do subs fixate harder so I can tell if its a distractor or not'
        
        - Retinal optic flow div/curl relative to COM trajectory (e.g. Matthis et al 2023), e.g. looking for retinal correlats of full-body steering
      
      - Visual Search - e.g. Najemnik/Geisler visual search stuff, e.g. likelihood of finding a target in a given area of the visual field (using RV1 model)



### Planned analysis
#### Biomechanics/musculoskeletal/mocap/physics/etc
##### Characterizing the preferred gait cycle
###### Walking speed
- Highest level variable big dum dum variable - most directly related to the 'task' (i.e. get yr body from here to there)
###### Step length
- defines basic 'compass gait' walker dynamics (e.g. Garcia et al 1995 or so? the 'simplest walking model' one), as step length is correlated with impact forces, etc
  - e.g. Kuo et al 2007, Donelan et al 2002, etc
###### Step timing
- somehow spinal CPGs + 'limb resonant frequency' related (e.g. Donelan stuff, that old paper about limb resonant frequencies - neville hogan or something? Holt? )
###### Step width
- less relevant to global physics/dynamics. Its more of a 'steering' thing (e.g. Bauby and Kuo 2000)
  - since the preferred path from A to B is a straight line, any M/L deviation is considered a 'cost'
  - Also, normal human step width is dang near 0 in free walking, so it will be pretty easy to measure deviations
  - also, `cross-over steps' with negative width are worth looking at!


##### COM vs BOS stuff
###### e.g. "energy recovery" per step (its in Matthis et al 2013)
###### e.g. Linear Inverted Pendulum "LIP" path deviation (i.e. estiamte COM traj from planted foot, see Koolen/Rebula/Pratt paper (and kinda `Matthis Fajen 2013`, but some of the basic physics is wrong there) 


#### Vision - Eye tracker stuff
- Oculomotor measures (i.e. where is the eye pointing from moment to moment? Cognitive decisions "output" side of the perception/output cycle. past decisions affect currently available information)
  - Inter-saccadic interval - How long are fixations? 
  - Sacade directions/magnitudes
    - Upward - looking ahead, search/goal
    - down - looking back <- flag for `per-action` analysis
    - L/R - search/foothold
    - large amplitude - 'new territory'
    - small amplitude - 'search within'
- Visual perceptual (image analysis, perceptual "available information", the 'input'arrow of the Perception Action Cycle - consequence of oculomotor decision)
  - Retinal flow analysis
  - RV1 (Najemnik Geisler) type analysis
  - This is the information being poured into the electric meatloaf

#### Integration - Gaze/Gait stuff

- e.g. look ahead distance - how far ahead are you looking (hypothesis - will vary with condition)
- e.g. look ahead time - how long until you get there (hypothetis - will be constant-ish around 1.5-2sec)
- e.g. the gaze/foothold nonsense from Matthis 2018 Current Bio


# Aim 2 - AUGMENTED REALITY GROUND PLANE - Laboratory-precision measurements of
visually-guided walking

## Rationale:

- Why do we need Laboratory-precision measurements?
  - Accuracy (can't trust kinematics of IMU systems)

      -and/or? - Maybe we can with the new `mesh` stuff, but we'll still want to validate against lab-based metrics?

  - Controllable/parameterizable terrain (can make contrived terrain configurations to test specific hypotheses)

  - Allows for hypothesis testing (outdoor work is 'quasi-observational' - good for *generating* hypotheses, indoor work necessary to *test* them)


## Methods: The Augmented Reality Ground-Plane (ARGP)

This is a souped up version of the thing Jon used for his disertation
References:
  - Matthis and Fajen 2013 (J Exp Psych: HPP)
  - Matthis and Fajen 2014 (Proceedings of the Royal Society B)
  - Matthis and Fajen 2015 (Journal of Vision)
  - Barton Matthis and Fajen 2017 (J Exp Psych: HPP)
  - Matthis, Barton and Fajen 2018 (PNAS)


The Augmented Reality Ground Plane (developed at Northeastern) is a projector-based, 14m-long indoor walking path. The content of the groundplane is displayed using a series of 3x ultra-short-throw projectors showing images from a Unity game engine that is streaming in realtime kinematic data via websocket. Note that the "realtime" streaming component only needs track feet, so it can be fast while we also record much higher spatial/temportal res videos for later analysis projectors and is real-time interactive, allowing for body-position-dependent updating of displayed terrain, and play real-time auditory feedback to the participant (this is essential for high accuracy footplacement)


For each of the experiments described below, we will recruit groups of participants (n\textgreater=10). 

## Planned Experiments
### Experiment #1 - Foothold density manipulation

- 5 levels of foothold density (dense = many footholds, easy; sparse = few footholds, difficult)
- Subject to standard experimental rigamarole
- identify behavioral profiles of each terrain type, use to ID behaviorally comparable terrains in the outdoor study

### Experiment 2 - Add distractors

  - Same as above, but with distractors (landault C's)

  - Variants
    - Constant visual density - Add enough distractors to each condition so the visual density is the same as the "dense" condition
    - Constant foothold density - Keep the foothold density the same, but add variable amount of distractors per condition (good for 'perceptual crowding' research, e.g. Bex)
    - Per target - Only put distractors around a sub-set of targets, use to determine how much peeps will deviate from PGC to avoid more difficult perceptual decisions
    - Manipulate perceptual difficulty - vary perceptual difference between target and disctract (e.g. via Landault C gap shrinking, or like, a contrast distinction (empty vs non-empty bullseyes), a semantic distinction (stepping on letters, vowels targets, consonants distractors), cognitive load (stepping on letters, must spell words; stepping on numbers only step on multiples of even numbers(easy), or multiples of 3(medium), 7(hard), etc )


### Experiment 3 - Contrived paths

  - Examine gaze/foothold patterns from Aim 1 and Exp 1/2 to determine 'typical' gaze patterns/path selections
  
  - Based on that, create arrangements with "dead-zones" (e.g. large sections of terrain without footholds), with and without "funnels" (i.e. a series of *perfect* steps that lead to a dead-zone)
  
    - examine gaze/gait patterns in these conditions to see when/if subjects notice the coming dead-zone, and how they react to it (i.e. big deviations from PGC (e.g. "whoopsie")? or do they see it coming and avoid more gracefully? cite Barton Matthis Fajen)
    
    - different gaze/gait patterns that occur in different cases (i.e. last-minute replan in a "whoopsie" vs. early replan in a graceful avoidance)
  
  - ALSO/OR - big swoopy curvy paths to look at planning on straight-aheads vs curves (help with the 'planning horizon' thing, because decouples look ahead from path planning due to curvature)
  
    - decouples end-goal planning from short-term step planning


