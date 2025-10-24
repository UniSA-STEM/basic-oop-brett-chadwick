"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <Brett Chadwick>
ID: <110407073>
Username: <chabx001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import Asset
class rig:
    def __init__(self, name, storage=[], damageCounter=0, broken=False, upgradeLevel = 0):
        self.name = name
        self.damageCounter = damageCounter
        self.broken = broken
        self.storage = storage
        self.upgradeLevel = upgradeLevel

    def set_rig(self):
        addition = self.storage + Asset("Data Spike", "idk")
        storage = self.storage + Asset("Data Spike", "idk")

    def set_broken(self):
        broken = self.broken

    def starting_kit(self):
        starting_spike = 0
        starting_drive = 0
        while starting_spike != 2:
            spike = Asset.Asset("Data Spike", "Spike")
            self.storage.append(spike)
            starting_spike = starting_spike + 1
        while starting_drive != 1:
            drive = Asset.Asset("Removable Drive", "Drive")
            self.storage.append(drive)
            starting_spike = starting_spike + 1
        print(f"Starting kit for hacker is {self.storage}")

    """Upgrades the rig if an upgrade chip is presernt"""
    def upgrade_rig(self, upgrade_chip):
        if upgrade_chip == False:
            return "cannot upgrade rig or something"
        else:
            self.upgradeLevel +=1
        return f"Rig level is now {self.upgradeLevel}"

