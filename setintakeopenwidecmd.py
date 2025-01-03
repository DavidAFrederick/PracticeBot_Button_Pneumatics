import wpilib
from commands2 import Command
from pneumaticsubsystem import PneumaticSubsystem


class SetIntakeOpenWideCmd(Command):
   def __init__(self, pneumaticsubsystem: PneumaticSubsystem):
       self.pneumaticsubsystem = pneumaticsubsystem

       self.addRequirements(self.pneumaticsubsystem)

   def initialize(self):
       super().initialize()

   def execute(self):
       self.pneumaticsubsystem.OpenIntake()
       print ("Intake - Open Wide")

   def isFinished(self) -> bool:
       return True

   def end(self, interrupted: bool):
       pass