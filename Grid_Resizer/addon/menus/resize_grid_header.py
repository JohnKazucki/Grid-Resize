import bpy

class GR_PT_AddMenu(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    bl_context = ".objectmode" 

    bl_label = "GridResizer"

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)

        row.operator("gridresizer.resizegridup", text="", icon="TRIA_UP")
        row.operator("gridresizer.resizegriddown", text="", icon="TRIA_DOWN")
        row.operator("gridresizer.resizegridreset", text="", icon="GRID")
        
