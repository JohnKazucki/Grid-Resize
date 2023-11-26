import bpy

from .resize_grid_header import GR_PT_AddMenu

classes = (
    GR_PT_AddMenu,
)


def register_menus():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_menus():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
