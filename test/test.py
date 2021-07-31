#_____The API Module____#
import neptune_lib as Neptune

descr = "Hi! This is My add-on" # This is The Description Variable for your project
icon = r"src/pack_icon.png" # The "pack_icon.png" Path for your project

#_____Project Properties____#

add_on = Neptune.create_project.CreateProject(4,"3")  #This Class Will create the project
add_on.create_dependencies(True, True) # This Method create the Behavior Pack/Ressource Pack

#_____Manifest Properties____#

add_on.project_version([1,7,1]) # The Project Version e.g('1.0.0','4.5.3')
add_on.project_properties(descr, icon) # Here You put a description & an icon for your project


# Neptune.createTexture("BLOCK","blockdummy","textureconng"