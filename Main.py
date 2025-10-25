import Hacker, Asset, Rig
"""
File: main.py
Description: <A brief description of this Python module.>
Author: <Brett Chadwick>
ID: <110407073>
Username: <chabx001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Main:
    #hacker = Hacker.hacker("L33T_G4M3R1234", inventory=Hacker.hacker.generate_inventory())
    #for i in hacker.inventory:
   #     print( f"The rig has a {Hacker.hacker.__str__(i)}")
    basic_rig = Rig.rig("Basic Rig",storage=[])
    print("rig created")
    basic_rig.starting_kit()
    """Starting kit testing"""
    for i in basic_rig.storage:
        print( f"The rig has a {Asset.asset.__str__(i)}")
    """Asset Generation testing"""
    basic_rig.generate_asset()
    for i in basic_rig.storage:
        print(f"The rig has a {Asset.asset.__str__(i)}")
    basic_rig.return_condition()



