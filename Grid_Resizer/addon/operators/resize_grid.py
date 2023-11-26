import bpy

from bpy.types import Operator



def set_grid_scale(mode):
    AREA = 'VIEW_3D'

    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if not area.type == AREA:
                continue

            for s in area.spaces:
                if s.type == AREA:
                    current_scale = s.overlay.grid_scale

                    if mode == "up":
                        s.overlay.grid_scale = current_scale*2
                    if mode == "down":
                        s.overlay.grid_scale = current_scale/2
                    if mode == "reset":
                        s.overlay.grid_scale = 1.0

                    break



class GR_OT_RESIZEGRIDUP(Operator):
    bl_idname = "gridresizer.resizegridup"
    bl_label = "Resize Grid Up"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        set_grid_scale("up")
        
        return {'FINISHED'}



class GR_OT_RESIZEGRIDDOWN(Operator):
    bl_idname = "gridresizer.resizegriddown"
    bl_label = "Resize Grid Down"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        set_grid_scale("down")
 
        return {'FINISHED'}
    

class GR_OT_RESIZEGRIDRESET(Operator):
    bl_idname = "gridresizer.resizegridreset"
    bl_label = "Reset Grid"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        set_grid_scale("reset")

        return {'FINISHED'}
    

