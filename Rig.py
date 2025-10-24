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

    def set_rig(self,starter_list):
     for i in starter_list:
         self.storage.append(starter_list[i])

    def upgrade_rig(self):

