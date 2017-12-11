from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -116.7
y = 7
z = -25.3
gift = mc.getBlock(x, y, z)

if gift == 57:
    mc.postToChat("Diamond is here")

elif gift == 6:
    mc.postToChat("Sapling is here")
    
else: 
    mc.postToChat("Bring a gift" + str(x) +"," + str(y) + "," +  str(z))
