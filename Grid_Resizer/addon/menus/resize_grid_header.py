import bpy

def draw_gr_toolbar(layout):
    row = layout.row(align=True)

    row.operator("gridresizer.resizegridup", text="", icon="TRIA_UP")
    row.operator("gridresizer.resizegriddown", text="", icon="TRIA_DOWN")
    row.operator("gridresizer.resizegridreset", text="", icon="GRID")

    current_scale = bpy.context.space_data.overlay.grid_scale
    row.separator()
    box = row.box()
    box.label(text="Scale: " + str(current_scale))


class GR_PT_TOOLBAR_OBJ(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    bl_context = ".objectmode" 

    bl_label = "GridResizer"

    def draw(self, context):
        draw_gr_toolbar(self.layout)

class GR_PT_TOOLBAR_EDITMESH(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    bl_context = ".mesh_edit" 

    bl_label = "GridResizer"

    def draw(self, context):
        draw_gr_toolbar(self.layout)