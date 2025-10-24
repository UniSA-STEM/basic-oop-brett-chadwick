"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <Brett Chadwick>
ID: <110407073>
Username: <chabx001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class rig:
    def __init__(self, name, storage=[], damageCounter=0, broken=False, upgradeLevel = 0):
        self.name = name
        self.damageCounter = damageCounter
        self.broken = broken
        self.storage = storage
        self.upgradeLevel = upgradeLevel

    def set_rig(self):
        storage = self.storage
    def set_broken(self):
        broken = self.broken

    """Upgrades the rig if an upgrade chip is presernt"""
    def upgrade_rig(self, upgrade_chip):
        if upgrade_chip ==False:
            return "cannot upgrade rig or something"
        else:
            self.upgradeLevel +=1
        return f"Rig level is now {self.upgradeLevel}"

