"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <Brett Chadwick>
ID: <110407073>
Username: <chabx001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class asset:
    def __init__(self, name, description, encrypted=False):
        self.name = name
        self.description = description
        self.encrypted = encrypted
    """Creates spike code, probably not neccessary"""
    #def create_spike(self,name="Data Spike", description="Throw this at enemies"):
     #   return self.name,self.description
    "Creates Crypto token"
    #def create_cryptotoken(self, name="Crypto Token", description="Used to acquire and repair rigs"):
     #   return self.name, self.description
    "Creates Removeable Drive"
    #def create_removeable_drive(self, name="Removeable Drive", description="Found in rigs and used for asset extraction"):
     #   return self.name, self.description
    "Creates Security Chip"
    #def create_security_chip(self, name="Security Chip", description="Used to encrypt and decrypt assets"):
     #   return self.name, self.description
    "Creates hardware patch"
    #def create_hardware_patch(self, name="Hardware Patch", description="Used for upgrading rigs"):
        #return self.name, self.description

    def __str__(self):
        return self.name
