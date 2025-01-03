import commands2
from commands2 import Subsystem
import wpilib

class PneumaticSubsystem(Subsystem):

    def __init__(self) -> None:
        super().__init__()      # Call the initialization routing of the parent Object
        print (">>>> Robot Initialization complete in __init__ in PneumaticSubsystem.py")

 # Compressor connected to a PH with a default CAN ID (1)
        self.compressor = wpilib.Compressor(wpilib.PneumaticsModuleType.CTREPCM)
               # DoubleSolenoid corresponds to a double solenoid.
        # In this case, it's connected to channels 1 and 2 of a PH with the default CAN ID.

        self.IntakeControl = wpilib.DoubleSolenoid(
            moduleType=wpilib.PneumaticsModuleType.CTREPCM,
            forwardChannel=0,
            reverseChannel=1,
        )

        self.gearboxSpeedControl = wpilib.DoubleSolenoid(
            moduleType=wpilib.PneumaticsModuleType.CTREPCM,
            forwardChannel=2,
            reverseChannel=3,
        )

        self.IntakeControl.set(wpilib.DoubleSolenoid.Value.kForward)
        self.gearboxSpeedControl.set(wpilib.DoubleSolenoid.Value.kForward)

    def OpenIntake(self):
        self.IntakeControl.set(wpilib.DoubleSolenoid.Value.kReverse)

    def CloseIntake(self):
        self.IntakeControl.set(wpilib.DoubleSolenoid.Value.kForward)

    def GearboxHighSpeed(self):
        self.gearboxSpeedControl.set(wpilib.DoubleSolenoid.Value.kForward)

    def GearboxLowSpeed(self):
        self.gearboxSpeedControl.set(wpilib.DoubleSolenoid.Value.kReverse)




        