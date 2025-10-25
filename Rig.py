"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <Brett Chadwick>
ID: <110407073>
Username: <chabx001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import Asset,random
class rig:
    def __init__(self, name, storage=[], damageCounter=0, broken=False, upgradeLevel = 0):
        self.name = name
        self.damageCounter = damageCounter
        self.broken = broken
        self.storage = storage
        self.upgradeLevel = upgradeLevel
    def set_broken(self,broken):
        broken = self.broken

    def set_name(self, name):
        name = self.name

    def set_damageCounter(self, damageCounter):
        damageCounter = self.damageCounter

    def set_storage(self, storage):
        storage = self.storage

    def set_upgradeLevel(self, upgradeLevel):
        upgradeLevel = self.upgradeLevel

    def get_name(self):
        return self.name

    def get_broken(self):
        return self.broken

    def get_damageCounter(self):
        return self.damageCounter

    def get_upgradeLevel(self):
        return self.upgradeLevel
    """Asset Generation code, uses switch statement python match??? seems cleaner than 5 if statements"""
    def generate_asset(self):
        rand = random.randint(1,5)
        match rand:
            case 1:
                return self.storage.append(Asset.asset("Crypto Token", "Used to acquire and repair rigs"))
            case 2:
                return self.storage.append(Asset.asset("Data Spike", "Used in battles"))
            case 3:
                return self.storage.append(Asset.asset("Removable Drive", "Found in rigs and used for asset extraction"))
            case 4:
                return self.storage.append(Asset.asset(name="Security Chip", description="Used to encrypt or decrypt assets"))
            case 5:
                return self.storage.append(Asset.asset(name="Hardware Patch", description="Used for upgrading rigs"))

    def return_condition(self):
        damage = self.damageCounter
        upgrade_level = self.upgradeLevel
        if upgrade_level == 0:
            match damage:
                case 0:
                    return damage == "Pristine"
                case 1:
                    return damage == "Damaged"
                case 2:
                    return damage == "Broken"

    def starting_kit(self):
        starting_spike = 0
        starting_drive = 0
        while starting_spike != 2:
            spike = Asset.asset("Data Spike", "Spike")
            self.storage.append(spike)
            starting_spike = starting_spike + 1
            print("Added Data Spike")
        while starting_drive != 1:
            drive = Asset.asset("Removable Drive", "Drive")
            self.storage.append(drive)
            starting_drive = starting_drive + 1
            print("added Removable Drive")
    """Upgrades the rig if an Hardware_Patch is presernt"""
    def upgrade_rig(self, Hardware_Patch):
        if Hardware_Patch != "Hardware Patch":
            return "cannot upgrade rig or something"
        else:
            self.upgradeLevel +=1
            return f"Rig level is now {self.upgradeLevel}"
    """Repairs the rig if the rig is damaged"""
    def repair_rig(self, cryptoToken):
        if self.broken == True:
            if cryptoToken in self.storage:
                self.damageCounter = 0
                print(f"Rig is damaged, repaired, current damage level = {self.damageCounter}")
        elif self.broken == False:
            print("no repairs are needed")
        elif cryptoToken not in self.storage:
            print("No crypto tokens to use for repairs")
        else:
            print("no repair is needed")

    def take_damage(self, data_spike):
        if data_spike is True:
            return self.damageCounter == self.damageCounter + 1



