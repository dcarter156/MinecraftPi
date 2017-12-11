from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = -116.7
shwrY = 29
shwrZ = 4

width = 5
height = 5
length = 5

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x < shwrX + width and po-op
    mc.setBlocks(shwrX, shwrY + height, shwrZ,
                shwrX + width, shwrY + height, shwrZ + length, 8)
else:
     mc.setBlocks(shwrX, shwrY + height, shwrZ,
                    shwrX + width, shwrY + height, shwrZ + length, 0)
