import bpy


# To better understand what values a keymap needs to work, check out this resource:
# https://github.com/brybalicious/toggle_mmb_numpad/blob/master/keymap_implementation.md
# It goes over all the possible Keymap Names, Region/Map/Space/Key Types, Values, etc.

# This implementation does not include the Region or Map Types
# For most use cases they are not very relevant, so they have been deliberately omitted here

keymaps =[
            # 3D View Keymaps
            {
                # Keymap name, this is one of 224 hardcoded strings from Blender
                "name": "3D View", 
                # Space Type, one of these https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items
                # This relates to the editor you wish to have the keymap work in. Such as the Node Editor or Console, etc.
                "space_type": "VIEW_3D", 
                # A list of KeyMap Items (kmi), each item being one shortcut
                "items":
                [
                    # grid resize up
                    {
                        "operator": "gridresizer.resizegridup", 
                        "type": "K",
                        "value": "PRESS",
                        # prop_name is not applicable for regular operators
                        # "prop_name": "", 
                        "shift": False,
                        "ctrl": False,
                        "alt": True,
                        "oskey": False,
                    },

                    # grid resize down
                    {
                        "operator": "gridresizer.resizegriddown", 
                        "type": "L",
                        "value": "PRESS",
                        # prop_name is not applicable for regular operators
                        # "prop_name": "", 
                        "shift": False,
                        "ctrl": False,
                        "alt": True,
                        "oskey": False,
                    },

                    # grid reset
                    {
                        "operator": "gridresizer.resizegridreset", 
                        "type": "M",
                        "value": "PRESS",
                        # prop_name is not applicable for regular operators
                        # "prop_name": "", 
                        "shift": False,
                        "ctrl": False,
                        "alt": True,
                        "oskey": False,
                    },
                ]
            },          
        ]


# to keep track of the custom keymaps this addon adds to Blender. These will be removed again when we unregister/disable the addon
keys = []



def register_keymap():

    wm = bpy.context.window_manager
    addon_keyconfig = wm.keyconfigs.addon

    kc = addon_keyconfig

    for keymap in keymaps:
        name = keymap["name"]
        space_type = keymap["space_type"]

        km = kc.keymaps.new(name=name, space_type=space_type)

        for item in keymap["items"]:
            operator = item["operator"]
            type = item["type"]
            value = item["value"]

            shift = item["shift"]
            ctrl = item["ctrl"]
            alt = item["alt"]
            oskey = item["oskey"]

            kmi = km.keymap_items.new(operator, type=type, value=value, shift=shift, ctrl=ctrl, alt=alt, oskey=oskey)

            if "prop_name" in item:
                kmi.properties.name = item["prop_name"]
            kmi.active = True

    keys.append((km, kmi))
    


def unregister_keymap():

    wm = bpy.context.window_manager

    for km, kmi in keys:
        km.keymap_items.remove(kmi)
    keys.clear()