from cx_Freeze import setup, Executable

setup(

    name="snake",

    version="1.0",

    description="Your application description",

    executables=[Executable("game.py")],

)   