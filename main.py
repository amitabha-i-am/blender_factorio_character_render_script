import bpy
import os

FILE_PATH = r"C:\tmp"
PATH_NAME = "idle_sniper"
PATH = os.path.join(FILE_PATH, PATH_NAME)
os.mkdir(PATH)
model = bpy.data.objects[1]
model.rotation_euler.z = 0
rotation_degree = 45
rotation_degree_rad = rotation_degree * 3.14159 / 180

for i in range(8):
    save_dir = os.path.join(PATH, str(i+1))
    os.mkdir(save_dir)
    bpy.context.scene.render.filepath = save_dir + "\\" + str(i+1)
    bpy.ops.render.render(animation=True, write_still=True)
    model.rotation_euler.z += -rotation_degree_rad
