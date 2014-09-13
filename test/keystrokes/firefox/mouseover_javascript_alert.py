#!/usr/bin/python

"""Test of Orca's support for mouseovers."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(KeyComboAction("<Control>Home"))
sequence.append(KeyComboAction("Down"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyPressAction(0, None, "KP_Insert"))
sequence.append(KeyComboAction("KP_Divide"))
sequence.append(KeyReleaseAction(0, None, "KP_Insert"))
sequence.append(utils.AssertPresentationAction(
    "1. Route the pointer to the image",
    ["BRAILLE LINE:  'Firefox application MouseOvers - Mozilla Firefox frame dialog'",
     "     VISIBLE:  'dialog', cursor=1",
     "BRAILLE LINE:  'Firefox application MouseOvers - Mozilla Firefox frame dialog OK push button'",
     "     VISIBLE:  'OK push button', cursor=1",
     "SPEECH OUTPUT: 'Welcome to mouseover-enabled Orca!'",
     "SPEECH OUTPUT: 'OK push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Escape"))
sequence.append(utils.AssertPresentationAction(
    "2. Escape to dismiss the dialog.",
    ["BRAILLE LINE:  'Orca Logo image'",
     "     VISIBLE:  'Orca Logo image', cursor=0",
     "SPEECH OUTPUT: 'Orca Logo image'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
