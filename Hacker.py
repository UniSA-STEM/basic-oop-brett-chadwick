"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <Brett Chadwick>
ID: <110407073>
Username: <chabx001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import Asset,Rig
class hacker:
    def __init__(self, name, inventory=[]):
        self.name = name
        self.inventory = inventory

    def get_name(self):
        return self.name
    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

    def set_name(self, name):
        self.name = name
    def add_rig(self, rig):
        self.inventory = rig + self.inventory

    def generate_inventory(self):
        self.inventory.append(Asset.asset("Crypto Token", "Token"))



