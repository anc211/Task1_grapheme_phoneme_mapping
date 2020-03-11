#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Wed Mar 11 09:17:59 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'grapheme_phoneme_mapping'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/anna/Dropbox (Personal)/0WORK@UPitt/Cerebellum_grant/experiment/Task1_grapheme_phoneme_mapping/grapheme_phoneme_mapping_v7_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[2048, 1152], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='cm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='In this task, you will learn ancient runes.\n\nYou will see a rune on the screen. Click on the speaker icon to hear how it is pronounced. Repeat after the speaker its pronunciation. You can listen to the sounds an unlimited number of times by clicking on the speaker icon. Try to remember the new rune and its pronunciation as best as you can.\n\nYou will practice all the runes 5 times. \n\nLet the experimenter know if you have any questions or press SPACE when you are ready to learn.',
    font='Arial',
    pos=(0, 0), height=0.7, wrapWidth=30, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instructions = keyboard.Keyboard()

# Initialize components for Routine "prompt_vowels"
prompt_vowelsClock = core.Clock()
text_prompt_vowels = visual.TextStim(win=win, name='text_prompt_vowels',
    text="Let's learn vowels!\n\nImportant! Some runes may represent different vowel sounds. \n\nPress SPACE to continue when you are ready.",
    font='Arial',
    pos=(0, 0), height=0.7, wrapWidth=1500, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_prompt_vowels = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank500 = visual.TextStim(win=win, name='blank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_intro"
trial_introClock = core.Clock()
image_rune_left1 = visual.ImageStim(
    win=win,
    name='image_rune_left1', 
    image='sin', mask=None,
    ori=0, pos=(-8, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
image_rune_right1 = visual.ImageStim(
    win=win,
    name='image_rune_right1', 
    image='sin', mask=None,
    ori=0, pos=(8, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
image_rune_mid1 = visual.ImageStim(
    win=win,
    name='image_rune_mid1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
sound_phoneme = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='sound_phoneme')
sound_phoneme.setVolume(1)
text_listen = visual.TextStim(win=win, name='text_listen',
    text='Listen!',
    font='Arial',
    pos=(0, 10), height=0.6, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "trial_practice"
trial_practiceClock = core.Clock()
image_rune_left = visual.ImageStim(
    win=win,
    name='image_rune_left', 
    image='sin', mask=None,
    ori=0, pos=(-8, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
image_rune_right = visual.ImageStim(
    win=win,
    name='image_rune_right', 
    image='sin', mask=None,
    ori=0, pos=(8, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
image_rune_mid = visual.ImageStim(
    win=win,
    name='image_rune_mid', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
image_speaker_left = visual.ImageStim(
    win=win,
    name='image_speaker_left', 
    image='sin', mask=None,
    ori=0, pos=(-8, -8), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_speaker_right = visual.ImageStim(
    win=win,
    name='image_speaker_right', 
    image='sin', mask=None,
    ori=0, pos=(8, -8), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_speaker_mid = visual.ImageStim(
    win=win,
    name='image_speaker_mid', 
    image='sin', mask=None,
    ori=0, pos=(0, -8), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text_practice = visual.TextStim(win=win, name='text_practice',
    text='Click on the speaker item to listen for the pronunciation of the rune as many times as you need.\nPress SPACE to move onto the next rune.',
    font='Arial',
    pos=(0, 10), height=0.6, wrapWidth=1500, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
key_select_sound = keyboard.Keyboard()
key_resp_next_trial = keyboard.Keyboard()
phoneme_practice1 = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='phoneme_practice1')
phoneme_practice1.setVolume(1)
phoneme_practice2 = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='phoneme_practice2')
phoneme_practice2.setVolume(1)

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank500 = visual.TextStim(win=win, name='blank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "prompt_consonants"
prompt_consonantsClock = core.Clock()
text_prompt_consonants = visual.TextStim(win=win, name='text_prompt_consonants',
    text="Let's learn consonants now!\n\nImportant! All consonant sounds can be spelled with two different runes!\n\nPress SPACE to continue when you are ready",
    font='Arial',
    pos=(0, 0), height=0.7, wrapWidth=1500, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_prompt_consonants = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank500 = visual.TextStim(win=win, name='blank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_intro"
trial_introClock = core.Clock()
image_rune_left1 = visual.ImageStim(
    win=win,
    name='image_rune_left1', 
    image='sin', mask=None,
    ori=0, pos=(-8, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
image_rune_right1 = visual.ImageStim(
    win=win,
    name='image_rune_right1', 
    image='sin', mask=None,
    ori=0, pos=(8, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
image_rune_mid1 = visual.ImageStim(
    win=win,
    name='image_rune_mid1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
sound_phoneme = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='sound_phoneme')
sound_phoneme.setVolume(1)
text_listen = visual.TextStim(win=win, name='text_listen',
    text='Listen!',
    font='Arial',
    pos=(0, 10), height=0.6, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "trial_practice"
trial_practiceClock = core.Clock()
image_rune_left = visual.ImageStim(
    win=win,
    name='image_rune_left', 
    image='sin', mask=None,
    ori=0, pos=(-8, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
image_rune_right = visual.ImageStim(
    win=win,
    name='image_rune_right', 
    image='sin', mask=None,
    ori=0, pos=(8, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
image_rune_mid = visual.ImageStim(
    win=win,
    name='image_rune_mid', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(8, 8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
image_speaker_left = visual.ImageStim(
    win=win,
    name='image_speaker_left', 
    image='sin', mask=None,
    ori=0, pos=(-8, -8), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_speaker_right = visual.ImageStim(
    win=win,
    name='image_speaker_right', 
    image='sin', mask=None,
    ori=0, pos=(8, -8), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_speaker_mid = visual.ImageStim(
    win=win,
    name='image_speaker_mid', 
    image='sin', mask=None,
    ori=0, pos=(0, -8), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text_practice = visual.TextStim(win=win, name='text_practice',
    text='Click on the speaker item to listen for the pronunciation of the rune as many times as you need.\nPress SPACE to move onto the next rune.',
    font='Arial',
    pos=(0, 10), height=0.6, wrapWidth=1500, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
key_select_sound = keyboard.Keyboard()
key_resp_next_trial = keyboard.Keyboard()
phoneme_practice1 = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='phoneme_practice1')
phoneme_practice1.setVolume(1)
phoneme_practice2 = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='phoneme_practice2')
phoneme_practice2.setVolume(1)

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank500 = visual.TextStim(win=win, name='blank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end_of_block"
end_of_blockClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You may take a break now\n\nPress SPACE to continue when you are ready',
    font='Arial',
    pos=(0, 0), height=0.7, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_continue = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
textz_end = visual.TextStim(win=win, name='textz_end',
    text='Thank you!\n\nLet the experimenter know that you are done.',
    font='Arial',
    pos=(0, 0), height=0.7, wrapWidth=30, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instructions.keys = []
key_resp_instructions.rt = []
_key_resp_instructions_allKeys = []
# keep track of which components have finished
instructionsComponents = [text_instructions, key_resp_instructions]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions* updates
    if text_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.tStart = t  # local t and not account for scr refresh
        text_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions, 'tStartRefresh')  # time at next scr refresh
        text_instructions.setAutoDraw(True)
    
    # *key_resp_instructions* updates
    waitOnFlip = False
    if key_resp_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instructions.frameNStart = frameN  # exact frame index
        key_resp_instructions.tStart = t  # local t and not account for scr refresh
        key_resp_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instructions.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instructions.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_instructions_allKeys.extend(theseKeys)
        if len(_key_resp_instructions_allKeys):
            key_resp_instructions.keys = _key_resp_instructions_allKeys[-1].name  # just the last key pressed
            key_resp_instructions.rt = _key_resp_instructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_instructions.started', text_instructions.tStartRefresh)
thisExp.addData('text_instructions.stopped', text_instructions.tStopRefresh)
# check responses
if key_resp_instructions.keys in ['', [], None]:  # No response was made
    key_resp_instructions.keys = None
thisExp.addData('key_resp_instructions.keys',key_resp_instructions.keys)
if key_resp_instructions.keys != None:  # we had a response
    thisExp.addData('key_resp_instructions.rt', key_resp_instructions.rt)
thisExp.addData('key_resp_instructions.started', key_resp_instructions.tStartRefresh)
thisExp.addData('key_resp_instructions.stopped', key_resp_instructions.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "prompt_vowels"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_prompt_vowels.keys = []
    key_resp_prompt_vowels.rt = []
    _key_resp_prompt_vowels_allKeys = []
    # keep track of which components have finished
    prompt_vowelsComponents = [text_prompt_vowels, key_resp_prompt_vowels]
    for thisComponent in prompt_vowelsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prompt_vowelsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prompt_vowels"-------
    while continueRoutine:
        # get current time
        t = prompt_vowelsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prompt_vowelsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_prompt_vowels* updates
        if text_prompt_vowels.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_prompt_vowels.frameNStart = frameN  # exact frame index
            text_prompt_vowels.tStart = t  # local t and not account for scr refresh
            text_prompt_vowels.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_prompt_vowels, 'tStartRefresh')  # time at next scr refresh
            text_prompt_vowels.setAutoDraw(True)
        
        # *key_resp_prompt_vowels* updates
        waitOnFlip = False
        if key_resp_prompt_vowels.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_prompt_vowels.frameNStart = frameN  # exact frame index
            key_resp_prompt_vowels.tStart = t  # local t and not account for scr refresh
            key_resp_prompt_vowels.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_prompt_vowels, 'tStartRefresh')  # time at next scr refresh
            key_resp_prompt_vowels.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_prompt_vowels.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_prompt_vowels.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_prompt_vowels.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_prompt_vowels.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_prompt_vowels_allKeys.extend(theseKeys)
            if len(_key_resp_prompt_vowels_allKeys):
                key_resp_prompt_vowels.keys = _key_resp_prompt_vowels_allKeys[-1].name  # just the last key pressed
                key_resp_prompt_vowels.rt = _key_resp_prompt_vowels_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prompt_vowelsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prompt_vowels"-------
    for thisComponent in prompt_vowelsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text_prompt_vowels.started', text_prompt_vowels.tStartRefresh)
    block.addData('text_prompt_vowels.stopped', text_prompt_vowels.tStopRefresh)
    # check responses
    if key_resp_prompt_vowels.keys in ['', [], None]:  # No response was made
        key_resp_prompt_vowels.keys = None
    block.addData('key_resp_prompt_vowels.keys',key_resp_prompt_vowels.keys)
    if key_resp_prompt_vowels.keys != None:  # we had a response
        block.addData('key_resp_prompt_vowels.rt', key_resp_prompt_vowels.rt)
    block.addData('key_resp_prompt_vowels.started', key_resp_prompt_vowels.tStartRefresh)
    block.addData('key_resp_prompt_vowels.stopped', key_resp_prompt_vowels.tStopRefresh)
    # the Routine "prompt_vowels" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_vowels = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trial_conditions_v5.csv', selection='0:4'),
        seed=None, name='trials_vowels')
    thisExp.addLoop(trials_vowels)  # add the loop to the experiment
    thisTrials_vowel = trials_vowels.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_vowel.rgb)
    if thisTrials_vowel != None:
        for paramName in thisTrials_vowel:
            exec('{} = thisTrials_vowel[paramName]'.format(paramName))
    
    for thisTrials_vowel in trials_vowels:
        currentLoop = trials_vowels
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_vowel.rgb)
        if thisTrials_vowel != None:
            for paramName in thisTrials_vowel:
                exec('{} = thisTrials_vowel[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "blank"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [blank500]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank500* updates
            if blank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank500.frameNStart = frameN  # exact frame index
                blank500.tStart = t  # local t and not account for scr refresh
                blank500.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank500, 'tStartRefresh')  # time at next scr refresh
                blank500.setAutoDraw(True)
            if blank500.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank500.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    blank500.tStop = t  # not accounting for scr refresh
                    blank500.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank500, 'tStopRefresh')  # time at next scr refresh
                    blank500.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blank"-------
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_vowels.addData('blank500.started', blank500.tStartRefresh)
        trials_vowels.addData('blank500.stopped', blank500.tStopRefresh)
        
        # ------Prepare to start Routine "trial_intro"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_rune_left1.setImage(pic1)
        image_rune_right1.setImage(pic2)
        image_rune_mid1.setImage(pic3)
        sound_phoneme.setSound(sound, hamming=False)
        sound_phoneme.setVolume(1, log=False)
        # keep track of which components have finished
        trial_introComponents = [image_rune_left1, image_rune_right1, image_rune_mid1, sound_phoneme, text_listen]
        for thisComponent in trial_introComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_intro"-------
        while continueRoutine:
            # get current time
            t = trial_introClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_introClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_rune_left1* updates
            if image_rune_left1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                image_rune_left1.frameNStart = frameN  # exact frame index
                image_rune_left1.tStart = t  # local t and not account for scr refresh
                image_rune_left1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_left1, 'tStartRefresh')  # time at next scr refresh
                image_rune_left1.setAutoDraw(True)
            if image_rune_left1.status == STARTED:
                if bool(sound_phoneme.status==FINISHED):
                    # keep track of stop time/frame for later
                    image_rune_left1.tStop = t  # not accounting for scr refresh
                    image_rune_left1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_rune_left1, 'tStopRefresh')  # time at next scr refresh
                    image_rune_left1.setAutoDraw(False)
            
            # *image_rune_right1* updates
            if image_rune_right1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                image_rune_right1.frameNStart = frameN  # exact frame index
                image_rune_right1.tStart = t  # local t and not account for scr refresh
                image_rune_right1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_right1, 'tStartRefresh')  # time at next scr refresh
                image_rune_right1.setAutoDraw(True)
            if image_rune_right1.status == STARTED:
                if bool(sound_phoneme.status==FINISHED):
                    # keep track of stop time/frame for later
                    image_rune_right1.tStop = t  # not accounting for scr refresh
                    image_rune_right1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_rune_right1, 'tStopRefresh')  # time at next scr refresh
                    image_rune_right1.setAutoDraw(False)
            
            # *image_rune_mid1* updates
            if image_rune_mid1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                image_rune_mid1.frameNStart = frameN  # exact frame index
                image_rune_mid1.tStart = t  # local t and not account for scr refresh
                image_rune_mid1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_mid1, 'tStartRefresh')  # time at next scr refresh
                image_rune_mid1.setAutoDraw(True)
            if image_rune_mid1.status == STARTED:
                if bool(sound_phoneme.status==FINISHED):
                    # keep track of stop time/frame for later
                    image_rune_mid1.tStop = t  # not accounting for scr refresh
                    image_rune_mid1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_rune_mid1, 'tStopRefresh')  # time at next scr refresh
                    image_rune_mid1.setAutoDraw(False)
            # start/stop sound_phoneme
            if sound_phoneme.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound_phoneme.frameNStart = frameN  # exact frame index
                sound_phoneme.tStart = t  # local t and not account for scr refresh
                sound_phoneme.tStartRefresh = tThisFlipGlobal  # on global time
                sound_phoneme.play()  # start the sound (it finishes automatically)
            
            # *text_listen* updates
            if text_listen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_listen.frameNStart = frameN  # exact frame index
                text_listen.tStart = t  # local t and not account for scr refresh
                text_listen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_listen, 'tStartRefresh')  # time at next scr refresh
                text_listen.setAutoDraw(True)
            if text_listen.status == STARTED:
                if bool(sound_phoneme.status==FINISHED):
                    # keep track of stop time/frame for later
                    text_listen.tStop = t  # not accounting for scr refresh
                    text_listen.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_listen, 'tStopRefresh')  # time at next scr refresh
                    text_listen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_introComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_intro"-------
        for thisComponent in trial_introComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_vowels.addData('image_rune_left1.started', image_rune_left1.tStartRefresh)
        trials_vowels.addData('image_rune_left1.stopped', image_rune_left1.tStopRefresh)
        trials_vowels.addData('image_rune_right1.started', image_rune_right1.tStartRefresh)
        trials_vowels.addData('image_rune_right1.stopped', image_rune_right1.tStopRefresh)
        trials_vowels.addData('image_rune_mid1.started', image_rune_mid1.tStartRefresh)
        trials_vowels.addData('image_rune_mid1.stopped', image_rune_mid1.tStopRefresh)
        sound_phoneme.stop()  # ensure sound has stopped at end of routine
        trials_vowels.addData('sound_phoneme.started', sound_phoneme.tStart)
        trials_vowels.addData('sound_phoneme.stopped', sound_phoneme.tStop)
        trials_vowels.addData('text_listen.started', text_listen.tStartRefresh)
        trials_vowels.addData('text_listen.stopped', text_listen.tStopRefresh)
        # the Routine "trial_intro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial_practice"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_rune_left.setImage(pic1)
        image_rune_right.setImage(pic2)
        image_rune_mid.setImage(pic3)
        image_speaker_left.setImage(image_icon1)
        image_speaker_right.setImage(image_icon2)
        image_speaker_mid.setImage(image_icon3)
        key_select_sound.keys = []
        key_select_sound.rt = []
        _key_select_sound_allKeys = []
        key_resp_next_trial.keys = []
        key_resp_next_trial.rt = []
        _key_resp_next_trial_allKeys = []
        phoneme_practice1.setSound(sound1, hamming=False)
        phoneme_practice1.setVolume(1, log=False)
        phoneme_practice2.setSound(sound2, hamming=False)
        phoneme_practice2.setVolume(1, log=False)
        # keep track of which components have finished
        trial_practiceComponents = [image_rune_left, image_rune_right, image_rune_mid, image_speaker_left, image_speaker_right, image_speaker_mid, text_practice, key_select_sound, key_resp_next_trial, phoneme_practice1, phoneme_practice2]
        for thisComponent in trial_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_practice"-------
        while continueRoutine:
            # get current time
            t = trial_practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_rune_left* updates
            if image_rune_left.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_rune_left.frameNStart = frameN  # exact frame index
                image_rune_left.tStart = t  # local t and not account for scr refresh
                image_rune_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_left, 'tStartRefresh')  # time at next scr refresh
                image_rune_left.setAutoDraw(True)
            
            # *image_rune_right* updates
            if image_rune_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_rune_right.frameNStart = frameN  # exact frame index
                image_rune_right.tStart = t  # local t and not account for scr refresh
                image_rune_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_right, 'tStartRefresh')  # time at next scr refresh
                image_rune_right.setAutoDraw(True)
            
            # *image_rune_mid* updates
            if image_rune_mid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_rune_mid.frameNStart = frameN  # exact frame index
                image_rune_mid.tStart = t  # local t and not account for scr refresh
                image_rune_mid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_mid, 'tStartRefresh')  # time at next scr refresh
                image_rune_mid.setAutoDraw(True)
            
            # *image_speaker_left* updates
            if image_speaker_left.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                image_speaker_left.frameNStart = frameN  # exact frame index
                image_speaker_left.tStart = t  # local t and not account for scr refresh
                image_speaker_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_speaker_left, 'tStartRefresh')  # time at next scr refresh
                image_speaker_left.setAutoDraw(True)
            
            # *image_speaker_right* updates
            if image_speaker_right.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                image_speaker_right.frameNStart = frameN  # exact frame index
                image_speaker_right.tStart = t  # local t and not account for scr refresh
                image_speaker_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_speaker_right, 'tStartRefresh')  # time at next scr refresh
                image_speaker_right.setAutoDraw(True)
            
            # *image_speaker_mid* updates
            if image_speaker_mid.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                image_speaker_mid.frameNStart = frameN  # exact frame index
                image_speaker_mid.tStart = t  # local t and not account for scr refresh
                image_speaker_mid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_speaker_mid, 'tStartRefresh')  # time at next scr refresh
                image_speaker_mid.setAutoDraw(True)
            
            # *text_practice* updates
            if text_practice.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                text_practice.frameNStart = frameN  # exact frame index
                text_practice.tStart = t  # local t and not account for scr refresh
                text_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_practice, 'tStartRefresh')  # time at next scr refresh
                text_practice.setAutoDraw(True)
            
            # *key_select_sound* updates
            waitOnFlip = False
            if key_select_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_select_sound.frameNStart = frameN  # exact frame index
                key_select_sound.tStart = t  # local t and not account for scr refresh
                key_select_sound.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_select_sound, 'tStartRefresh')  # time at next scr refresh
                key_select_sound.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_select_sound.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_select_sound.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_select_sound.status == STARTED and not waitOnFlip:
                theseKeys = key_select_sound.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_select_sound_allKeys.extend(theseKeys)
                if len(_key_select_sound_allKeys):
                    key_select_sound.keys = _key_select_sound_allKeys[0].name  # just the first key pressed
                    key_select_sound.rt = _key_select_sound_allKeys[0].rt
            
            # *key_resp_next_trial* updates
            waitOnFlip = False
            if key_resp_next_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_next_trial.frameNStart = frameN  # exact frame index
                key_resp_next_trial.tStart = t  # local t and not account for scr refresh
                key_resp_next_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_next_trial, 'tStartRefresh')  # time at next scr refresh
                key_resp_next_trial.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_next_trial.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_next_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_next_trial.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_next_trial.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_next_trial_allKeys.extend(theseKeys)
                if len(_key_resp_next_trial_allKeys):
                    key_resp_next_trial.keys = _key_resp_next_trial_allKeys[0].name  # just the first key pressed
                    key_resp_next_trial.rt = _key_resp_next_trial_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            # start/stop phoneme_practice1
            if phoneme_practice1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                phoneme_practice1.frameNStart = frameN  # exact frame index
                phoneme_practice1.tStart = t  # local t and not account for scr refresh
                phoneme_practice1.tStartRefresh = tThisFlipGlobal  # on global time
                phoneme_practice1.play(when=win)  # sync with win flip
            # start/stop phoneme_practice2
            if phoneme_practice2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                phoneme_practice2.frameNStart = frameN  # exact frame index
                phoneme_practice2.tStart = t  # local t and not account for scr refresh
                phoneme_practice2.tStartRefresh = tThisFlipGlobal  # on global time
                phoneme_practice2.play(when=win)  # sync with win flip
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_practice"-------
        for thisComponent in trial_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_vowels.addData('image_rune_left.started', image_rune_left.tStartRefresh)
        trials_vowels.addData('image_rune_left.stopped', image_rune_left.tStopRefresh)
        trials_vowels.addData('image_rune_right.started', image_rune_right.tStartRefresh)
        trials_vowels.addData('image_rune_right.stopped', image_rune_right.tStopRefresh)
        trials_vowels.addData('image_rune_mid.started', image_rune_mid.tStartRefresh)
        trials_vowels.addData('image_rune_mid.stopped', image_rune_mid.tStopRefresh)
        trials_vowels.addData('image_speaker_left.started', image_speaker_left.tStartRefresh)
        trials_vowels.addData('image_speaker_left.stopped', image_speaker_left.tStopRefresh)
        trials_vowels.addData('image_speaker_right.started', image_speaker_right.tStartRefresh)
        trials_vowels.addData('image_speaker_right.stopped', image_speaker_right.tStopRefresh)
        trials_vowels.addData('image_speaker_mid.started', image_speaker_mid.tStartRefresh)
        trials_vowels.addData('image_speaker_mid.stopped', image_speaker_mid.tStopRefresh)
        trials_vowels.addData('text_practice.started', text_practice.tStartRefresh)
        trials_vowels.addData('text_practice.stopped', text_practice.tStopRefresh)
        # check responses
        if key_select_sound.keys in ['', [], None]:  # No response was made
            key_select_sound.keys = None
        trials_vowels.addData('key_select_sound.keys',key_select_sound.keys)
        if key_select_sound.keys != None:  # we had a response
            trials_vowels.addData('key_select_sound.rt', key_select_sound.rt)
        trials_vowels.addData('key_select_sound.started', key_select_sound.tStartRefresh)
        trials_vowels.addData('key_select_sound.stopped', key_select_sound.tStopRefresh)
        # check responses
        if key_resp_next_trial.keys in ['', [], None]:  # No response was made
            key_resp_next_trial.keys = None
        trials_vowels.addData('key_resp_next_trial.keys',key_resp_next_trial.keys)
        if key_resp_next_trial.keys != None:  # we had a response
            trials_vowels.addData('key_resp_next_trial.rt', key_resp_next_trial.rt)
        trials_vowels.addData('key_resp_next_trial.started', key_resp_next_trial.tStartRefresh)
        trials_vowels.addData('key_resp_next_trial.stopped', key_resp_next_trial.tStopRefresh)
        phoneme_practice1.stop()  # ensure sound has stopped at end of routine
        trials_vowels.addData('phoneme_practice1.started', phoneme_practice1.tStartRefresh)
        trials_vowels.addData('phoneme_practice1.stopped', phoneme_practice1.tStopRefresh)
        phoneme_practice2.stop()  # ensure sound has stopped at end of routine
        trials_vowels.addData('phoneme_practice2.started', phoneme_practice2.tStartRefresh)
        trials_vowels.addData('phoneme_practice2.stopped', phoneme_practice2.tStopRefresh)
        # the Routine "trial_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "blank"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [blank500]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank500* updates
            if blank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank500.frameNStart = frameN  # exact frame index
                blank500.tStart = t  # local t and not account for scr refresh
                blank500.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank500, 'tStartRefresh')  # time at next scr refresh
                blank500.setAutoDraw(True)
            if blank500.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank500.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    blank500.tStop = t  # not accounting for scr refresh
                    blank500.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank500, 'tStopRefresh')  # time at next scr refresh
                    blank500.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blank"-------
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_vowels.addData('blank500.started', blank500.tStartRefresh)
        trials_vowels.addData('blank500.stopped', blank500.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_vowels'
    
    
    # ------Prepare to start Routine "prompt_consonants"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_prompt_consonants.keys = []
    key_resp_prompt_consonants.rt = []
    _key_resp_prompt_consonants_allKeys = []
    # keep track of which components have finished
    prompt_consonantsComponents = [text_prompt_consonants, key_resp_prompt_consonants]
    for thisComponent in prompt_consonantsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prompt_consonantsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prompt_consonants"-------
    while continueRoutine:
        # get current time
        t = prompt_consonantsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prompt_consonantsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_prompt_consonants* updates
        if text_prompt_consonants.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_prompt_consonants.frameNStart = frameN  # exact frame index
            text_prompt_consonants.tStart = t  # local t and not account for scr refresh
            text_prompt_consonants.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_prompt_consonants, 'tStartRefresh')  # time at next scr refresh
            text_prompt_consonants.setAutoDraw(True)
        
        # *key_resp_prompt_consonants* updates
        waitOnFlip = False
        if key_resp_prompt_consonants.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_prompt_consonants.frameNStart = frameN  # exact frame index
            key_resp_prompt_consonants.tStart = t  # local t and not account for scr refresh
            key_resp_prompt_consonants.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_prompt_consonants, 'tStartRefresh')  # time at next scr refresh
            key_resp_prompt_consonants.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_prompt_consonants.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_prompt_consonants.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_prompt_consonants.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_prompt_consonants.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_prompt_consonants_allKeys.extend(theseKeys)
            if len(_key_resp_prompt_consonants_allKeys):
                key_resp_prompt_consonants.keys = _key_resp_prompt_consonants_allKeys[-1].name  # just the last key pressed
                key_resp_prompt_consonants.rt = _key_resp_prompt_consonants_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prompt_consonantsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prompt_consonants"-------
    for thisComponent in prompt_consonantsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text_prompt_consonants.started', text_prompt_consonants.tStartRefresh)
    block.addData('text_prompt_consonants.stopped', text_prompt_consonants.tStopRefresh)
    # check responses
    if key_resp_prompt_consonants.keys in ['', [], None]:  # No response was made
        key_resp_prompt_consonants.keys = None
    block.addData('key_resp_prompt_consonants.keys',key_resp_prompt_consonants.keys)
    if key_resp_prompt_consonants.keys != None:  # we had a response
        block.addData('key_resp_prompt_consonants.rt', key_resp_prompt_consonants.rt)
    block.addData('key_resp_prompt_consonants.started', key_resp_prompt_consonants.tStartRefresh)
    block.addData('key_resp_prompt_consonants.stopped', key_resp_prompt_consonants.tStopRefresh)
    # the Routine "prompt_consonants" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_consonants = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trial_conditions_v5.csv', selection='4:14'),
        seed=None, name='trials_consonants')
    thisExp.addLoop(trials_consonants)  # add the loop to the experiment
    thisTrials_consonant = trials_consonants.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_consonant.rgb)
    if thisTrials_consonant != None:
        for paramName in thisTrials_consonant:
            exec('{} = thisTrials_consonant[paramName]'.format(paramName))
    
    for thisTrials_consonant in trials_consonants:
        currentLoop = trials_consonants
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_consonant.rgb)
        if thisTrials_consonant != None:
            for paramName in thisTrials_consonant:
                exec('{} = thisTrials_consonant[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "blank"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [blank500]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank500* updates
            if blank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank500.frameNStart = frameN  # exact frame index
                blank500.tStart = t  # local t and not account for scr refresh
                blank500.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank500, 'tStartRefresh')  # time at next scr refresh
                blank500.setAutoDraw(True)
            if blank500.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank500.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    blank500.tStop = t  # not accounting for scr refresh
                    blank500.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank500, 'tStopRefresh')  # time at next scr refresh
                    blank500.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blank"-------
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_consonants.addData('blank500.started', blank500.tStartRefresh)
        trials_consonants.addData('blank500.stopped', blank500.tStopRefresh)
        
        # ------Prepare to start Routine "trial_intro"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_rune_left1.setImage(pic1)
        image_rune_right1.setImage(pic2)
        image_rune_mid1.setImage(pic3)
        sound_phoneme.setSound(sound, hamming=False)
        sound_phoneme.setVolume(1, log=False)
        # keep track of which components have finished
        trial_introComponents = [image_rune_left1, image_rune_right1, image_rune_mid1, sound_phoneme, text_listen]
        for thisComponent in trial_introComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_intro"-------
        while continueRoutine:
            # get current time
            t = trial_introClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_introClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_rune_left1* updates
            if image_rune_left1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                image_rune_left1.frameNStart = frameN  # exact frame index
                image_rune_left1.tStart = t  # local t and not account for scr refresh
                image_rune_left1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_left1, 'tStartRefresh')  # time at next scr refresh
                image_rune_left1.setAutoDraw(True)
            if image_rune_left1.status == STARTED:
                if bool(sound_phoneme.status==FINISHED):
                    # keep track of stop time/frame for later
                    image_rune_left1.tStop = t  # not accounting for scr refresh
                    image_rune_left1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_rune_left1, 'tStopRefresh')  # time at next scr refresh
                    image_rune_left1.setAutoDraw(False)
            
            # *image_rune_right1* updates
            if image_rune_right1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                image_rune_right1.frameNStart = frameN  # exact frame index
                image_rune_right1.tStart = t  # local t and not account for scr refresh
                image_rune_right1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_right1, 'tStartRefresh')  # time at next scr refresh
                image_rune_right1.setAutoDraw(True)
            if image_rune_right1.status == STARTED:
                if bool(sound_phoneme.status==FINISHED):
                    # keep track of stop time/frame for later
                    image_rune_right1.tStop = t  # not accounting for scr refresh
                    image_rune_right1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_rune_right1, 'tStopRefresh')  # time at next scr refresh
                    image_rune_right1.setAutoDraw(False)
            
            # *image_rune_mid1* updates
            if image_rune_mid1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                image_rune_mid1.frameNStart = frameN  # exact frame index
                image_rune_mid1.tStart = t  # local t and not account for scr refresh
                image_rune_mid1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_mid1, 'tStartRefresh')  # time at next scr refresh
                image_rune_mid1.setAutoDraw(True)
            if image_rune_mid1.status == STARTED:
                if bool(sound_phoneme.status==FINISHED):
                    # keep track of stop time/frame for later
                    image_rune_mid1.tStop = t  # not accounting for scr refresh
                    image_rune_mid1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_rune_mid1, 'tStopRefresh')  # time at next scr refresh
                    image_rune_mid1.setAutoDraw(False)
            # start/stop sound_phoneme
            if sound_phoneme.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound_phoneme.frameNStart = frameN  # exact frame index
                sound_phoneme.tStart = t  # local t and not account for scr refresh
                sound_phoneme.tStartRefresh = tThisFlipGlobal  # on global time
                sound_phoneme.play()  # start the sound (it finishes automatically)
            
            # *text_listen* updates
            if text_listen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_listen.frameNStart = frameN  # exact frame index
                text_listen.tStart = t  # local t and not account for scr refresh
                text_listen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_listen, 'tStartRefresh')  # time at next scr refresh
                text_listen.setAutoDraw(True)
            if text_listen.status == STARTED:
                if bool(sound_phoneme.status==FINISHED):
                    # keep track of stop time/frame for later
                    text_listen.tStop = t  # not accounting for scr refresh
                    text_listen.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_listen, 'tStopRefresh')  # time at next scr refresh
                    text_listen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_introComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_intro"-------
        for thisComponent in trial_introComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_consonants.addData('image_rune_left1.started', image_rune_left1.tStartRefresh)
        trials_consonants.addData('image_rune_left1.stopped', image_rune_left1.tStopRefresh)
        trials_consonants.addData('image_rune_right1.started', image_rune_right1.tStartRefresh)
        trials_consonants.addData('image_rune_right1.stopped', image_rune_right1.tStopRefresh)
        trials_consonants.addData('image_rune_mid1.started', image_rune_mid1.tStartRefresh)
        trials_consonants.addData('image_rune_mid1.stopped', image_rune_mid1.tStopRefresh)
        sound_phoneme.stop()  # ensure sound has stopped at end of routine
        trials_consonants.addData('sound_phoneme.started', sound_phoneme.tStart)
        trials_consonants.addData('sound_phoneme.stopped', sound_phoneme.tStop)
        trials_consonants.addData('text_listen.started', text_listen.tStartRefresh)
        trials_consonants.addData('text_listen.stopped', text_listen.tStopRefresh)
        # the Routine "trial_intro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial_practice"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_rune_left.setImage(pic1)
        image_rune_right.setImage(pic2)
        image_rune_mid.setImage(pic3)
        image_speaker_left.setImage(image_icon1)
        image_speaker_right.setImage(image_icon2)
        image_speaker_mid.setImage(image_icon3)
        key_select_sound.keys = []
        key_select_sound.rt = []
        _key_select_sound_allKeys = []
        key_resp_next_trial.keys = []
        key_resp_next_trial.rt = []
        _key_resp_next_trial_allKeys = []
        phoneme_practice1.setSound(sound1, hamming=False)
        phoneme_practice1.setVolume(1, log=False)
        phoneme_practice2.setSound(sound2, hamming=False)
        phoneme_practice2.setVolume(1, log=False)
        # keep track of which components have finished
        trial_practiceComponents = [image_rune_left, image_rune_right, image_rune_mid, image_speaker_left, image_speaker_right, image_speaker_mid, text_practice, key_select_sound, key_resp_next_trial, phoneme_practice1, phoneme_practice2]
        for thisComponent in trial_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_practice"-------
        while continueRoutine:
            # get current time
            t = trial_practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_rune_left* updates
            if image_rune_left.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_rune_left.frameNStart = frameN  # exact frame index
                image_rune_left.tStart = t  # local t and not account for scr refresh
                image_rune_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_left, 'tStartRefresh')  # time at next scr refresh
                image_rune_left.setAutoDraw(True)
            
            # *image_rune_right* updates
            if image_rune_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_rune_right.frameNStart = frameN  # exact frame index
                image_rune_right.tStart = t  # local t and not account for scr refresh
                image_rune_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_right, 'tStartRefresh')  # time at next scr refresh
                image_rune_right.setAutoDraw(True)
            
            # *image_rune_mid* updates
            if image_rune_mid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_rune_mid.frameNStart = frameN  # exact frame index
                image_rune_mid.tStart = t  # local t and not account for scr refresh
                image_rune_mid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rune_mid, 'tStartRefresh')  # time at next scr refresh
                image_rune_mid.setAutoDraw(True)
            
            # *image_speaker_left* updates
            if image_speaker_left.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                image_speaker_left.frameNStart = frameN  # exact frame index
                image_speaker_left.tStart = t  # local t and not account for scr refresh
                image_speaker_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_speaker_left, 'tStartRefresh')  # time at next scr refresh
                image_speaker_left.setAutoDraw(True)
            
            # *image_speaker_right* updates
            if image_speaker_right.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                image_speaker_right.frameNStart = frameN  # exact frame index
                image_speaker_right.tStart = t  # local t and not account for scr refresh
                image_speaker_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_speaker_right, 'tStartRefresh')  # time at next scr refresh
                image_speaker_right.setAutoDraw(True)
            
            # *image_speaker_mid* updates
            if image_speaker_mid.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                image_speaker_mid.frameNStart = frameN  # exact frame index
                image_speaker_mid.tStart = t  # local t and not account for scr refresh
                image_speaker_mid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_speaker_mid, 'tStartRefresh')  # time at next scr refresh
                image_speaker_mid.setAutoDraw(True)
            
            # *text_practice* updates
            if text_practice.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                text_practice.frameNStart = frameN  # exact frame index
                text_practice.tStart = t  # local t and not account for scr refresh
                text_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_practice, 'tStartRefresh')  # time at next scr refresh
                text_practice.setAutoDraw(True)
            
            # *key_select_sound* updates
            waitOnFlip = False
            if key_select_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_select_sound.frameNStart = frameN  # exact frame index
                key_select_sound.tStart = t  # local t and not account for scr refresh
                key_select_sound.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_select_sound, 'tStartRefresh')  # time at next scr refresh
                key_select_sound.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_select_sound.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_select_sound.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_select_sound.status == STARTED and not waitOnFlip:
                theseKeys = key_select_sound.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_select_sound_allKeys.extend(theseKeys)
                if len(_key_select_sound_allKeys):
                    key_select_sound.keys = _key_select_sound_allKeys[0].name  # just the first key pressed
                    key_select_sound.rt = _key_select_sound_allKeys[0].rt
            
            # *key_resp_next_trial* updates
            waitOnFlip = False
            if key_resp_next_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_next_trial.frameNStart = frameN  # exact frame index
                key_resp_next_trial.tStart = t  # local t and not account for scr refresh
                key_resp_next_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_next_trial, 'tStartRefresh')  # time at next scr refresh
                key_resp_next_trial.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_next_trial.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_next_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_next_trial.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_next_trial.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_next_trial_allKeys.extend(theseKeys)
                if len(_key_resp_next_trial_allKeys):
                    key_resp_next_trial.keys = _key_resp_next_trial_allKeys[0].name  # just the first key pressed
                    key_resp_next_trial.rt = _key_resp_next_trial_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            # start/stop phoneme_practice1
            if phoneme_practice1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                phoneme_practice1.frameNStart = frameN  # exact frame index
                phoneme_practice1.tStart = t  # local t and not account for scr refresh
                phoneme_practice1.tStartRefresh = tThisFlipGlobal  # on global time
                phoneme_practice1.play(when=win)  # sync with win flip
            # start/stop phoneme_practice2
            if phoneme_practice2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                phoneme_practice2.frameNStart = frameN  # exact frame index
                phoneme_practice2.tStart = t  # local t and not account for scr refresh
                phoneme_practice2.tStartRefresh = tThisFlipGlobal  # on global time
                phoneme_practice2.play(when=win)  # sync with win flip
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_practice"-------
        for thisComponent in trial_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_consonants.addData('image_rune_left.started', image_rune_left.tStartRefresh)
        trials_consonants.addData('image_rune_left.stopped', image_rune_left.tStopRefresh)
        trials_consonants.addData('image_rune_right.started', image_rune_right.tStartRefresh)
        trials_consonants.addData('image_rune_right.stopped', image_rune_right.tStopRefresh)
        trials_consonants.addData('image_rune_mid.started', image_rune_mid.tStartRefresh)
        trials_consonants.addData('image_rune_mid.stopped', image_rune_mid.tStopRefresh)
        trials_consonants.addData('image_speaker_left.started', image_speaker_left.tStartRefresh)
        trials_consonants.addData('image_speaker_left.stopped', image_speaker_left.tStopRefresh)
        trials_consonants.addData('image_speaker_right.started', image_speaker_right.tStartRefresh)
        trials_consonants.addData('image_speaker_right.stopped', image_speaker_right.tStopRefresh)
        trials_consonants.addData('image_speaker_mid.started', image_speaker_mid.tStartRefresh)
        trials_consonants.addData('image_speaker_mid.stopped', image_speaker_mid.tStopRefresh)
        trials_consonants.addData('text_practice.started', text_practice.tStartRefresh)
        trials_consonants.addData('text_practice.stopped', text_practice.tStopRefresh)
        # check responses
        if key_select_sound.keys in ['', [], None]:  # No response was made
            key_select_sound.keys = None
        trials_consonants.addData('key_select_sound.keys',key_select_sound.keys)
        if key_select_sound.keys != None:  # we had a response
            trials_consonants.addData('key_select_sound.rt', key_select_sound.rt)
        trials_consonants.addData('key_select_sound.started', key_select_sound.tStartRefresh)
        trials_consonants.addData('key_select_sound.stopped', key_select_sound.tStopRefresh)
        # check responses
        if key_resp_next_trial.keys in ['', [], None]:  # No response was made
            key_resp_next_trial.keys = None
        trials_consonants.addData('key_resp_next_trial.keys',key_resp_next_trial.keys)
        if key_resp_next_trial.keys != None:  # we had a response
            trials_consonants.addData('key_resp_next_trial.rt', key_resp_next_trial.rt)
        trials_consonants.addData('key_resp_next_trial.started', key_resp_next_trial.tStartRefresh)
        trials_consonants.addData('key_resp_next_trial.stopped', key_resp_next_trial.tStopRefresh)
        phoneme_practice1.stop()  # ensure sound has stopped at end of routine
        trials_consonants.addData('phoneme_practice1.started', phoneme_practice1.tStartRefresh)
        trials_consonants.addData('phoneme_practice1.stopped', phoneme_practice1.tStopRefresh)
        phoneme_practice2.stop()  # ensure sound has stopped at end of routine
        trials_consonants.addData('phoneme_practice2.started', phoneme_practice2.tStartRefresh)
        trials_consonants.addData('phoneme_practice2.stopped', phoneme_practice2.tStopRefresh)
        # the Routine "trial_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "blank"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [blank500]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank500* updates
            if blank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank500.frameNStart = frameN  # exact frame index
                blank500.tStart = t  # local t and not account for scr refresh
                blank500.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank500, 'tStartRefresh')  # time at next scr refresh
                blank500.setAutoDraw(True)
            if blank500.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank500.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    blank500.tStop = t  # not accounting for scr refresh
                    blank500.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank500, 'tStopRefresh')  # time at next scr refresh
                    blank500.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blank"-------
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_consonants.addData('blank500.started', blank500.tStartRefresh)
        trials_consonants.addData('blank500.stopped', blank500.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_consonants'
    
    
    # ------Prepare to start Routine "end_of_block"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_continue.keys = []
    key_continue.rt = []
    _key_continue_allKeys = []
    # keep track of which components have finished
    end_of_blockComponents = [text, key_continue]
    for thisComponent in end_of_blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_of_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_of_block"-------
    while continueRoutine:
        # get current time
        t = end_of_blockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_of_blockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_continue* updates
        waitOnFlip = False
        if key_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_continue.frameNStart = frameN  # exact frame index
            key_continue.tStart = t  # local t and not account for scr refresh
            key_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_continue, 'tStartRefresh')  # time at next scr refresh
            key_continue.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_continue.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_continue.status == STARTED and not waitOnFlip:
            theseKeys = key_continue.getKeys(keyList=['space'], waitRelease=False)
            _key_continue_allKeys.extend(theseKeys)
            if len(_key_continue_allKeys):
                key_continue.keys = _key_continue_allKeys[-1].name  # just the last key pressed
                key_continue.rt = _key_continue_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_of_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_of_block"-------
    for thisComponent in end_of_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text.started', text.tStartRefresh)
    block.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_continue.keys in ['', [], None]:  # No response was made
        key_continue.keys = None
    block.addData('key_continue.keys',key_continue.keys)
    if key_continue.keys != None:  # we had a response
        block.addData('key_continue.rt', key_continue.rt)
    block.addData('key_continue.started', key_continue.tStartRefresh)
    block.addData('key_continue.stopped', key_continue.tStopRefresh)
    # the Routine "end_of_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 5 repeats of 'block'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [textz_end]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textz_end* updates
    if textz_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textz_end.frameNStart = frameN  # exact frame index
        textz_end.tStart = t  # local t and not account for scr refresh
        textz_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textz_end, 'tStartRefresh')  # time at next scr refresh
        textz_end.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textz_end.started', textz_end.tStartRefresh)
thisExp.addData('textz_end.stopped', textz_end.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
