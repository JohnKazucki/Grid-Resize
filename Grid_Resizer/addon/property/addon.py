import bpy

import rna_keymap_ui

from ..utility.addon import addon_name



class GR_Props(bpy.types.AddonPreferences):
    bl_idname = addon_name

    def draw(self, context):


        layout = self.layout

        box = layout.box()

        col = box.column()

        # huge thanks to Kilbee for their keymap preferences drawing method found here: 
        # https://blenderartists.org/t/keymap-for-addons/685544/6
        # https://github.com/kilbee/kbPIEs/blob/e7070e591d157aabfeb554366c317c1cf121b4bf/kbPIEs.py#L36
        
        # instead of iterating over the km, kmi that were added during registration of the addon keymaps
        # we look for those registered keymaps in the keyconfigs.user kc, by checking their property name, and draw them in the preferences

        # SINGLE KEYMAP EXAMPLE
        # km = kc.keymaps['3D View']
        # kmi = get_hotkey_entry_item(km, "wm.call_menu_pie", "RBM_MT_Bevel_Menu")
        # if kmi:
        #     col.context_pointer_set("keymap", km)
        #     rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)

        kc = context.window_manager.keyconfigs.user

        from ..registration.keymap import keymaps

        for keymap in keymaps:
            name = keymap["name"]
            km = kc.keymaps[name]

            col.label(text=name)

            for item in keymap["items"]:

                kmi = get_hotkey_entry_item(km, item)

                if kmi:
                    col.context_pointer_set("keymap", km)
                    # draw the keymap item in the Addon Preferences menu
                    # Sadly there is no documentation for this module or function currently
                    rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)


# huge thanks to Kilbee for their keymap preferences drawing method
# see the AddonPreferences draw function for the context/use of this function
def get_hotkey_entry_item(km, item):
    '''
    returns hotkey of specific type, with specific operator name and  optionally properties.name (keymap is not a dict, so referencing by keys is not enough
    if there are multiple hotkeys!)
    '''

    kmi_name = item["operator"]
    
    for i, km_item in enumerate(km.keymap_items):
        if km.keymap_items.keys()[i] == kmi_name:
            if "prop_name" in item:
                kmi_value = item["prop_name"]
                if km.keymap_items[i].properties.name == kmi_value:
                    return km_item
            return km_item
    return None # not needed, since no return means None, but keeping for readability