import bpy

from .resize_grid import GR_OT_RESIZEGRIDUP, GR_OT_RESIZEGRIDDOWN, GR_OT_RESIZEGRIDRESET

classes = (
    GR_OT_RESIZEGRIDUP, GR_OT_RESIZEGRIDDOWN, GR_OT_RESIZEGRIDRESET
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
