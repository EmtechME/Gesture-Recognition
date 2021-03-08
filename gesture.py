import numpy as np


def handData(handValues,side):

  #Extract Value and give names
  wrist=handValues[0]
  thumbMCP=handValues[2]
  thumbTip = handValues[4]
  pinkyMCP=handValues[17]
  orientation=''
  fingerTipX=[]
  fingerTipY=[]
  MCPX=[]
  MCPY=[]

  # Finger tip value collection
  for x in range (8,24 ,4):
    fingerTipX.append(handValues[x].x)
    fingerTipY.append(handValues[x].y)

  #MCP Values collection
  for x in range(5, 21, 4):
    MCPX.append(handValues[x].x)
    MCPY.append(handValues[x].y)

  MCPX=np.array(MCPX)
  MCPY=np.array(MCPY)

  # detection of orientation of Hand
  if wrist.y < thumbMCP.y and wrist.y < pinkyMCP.y:
    print("hand pointing to Down")
    orientation = 'down'
  elif wrist.x < thumbMCP.x and wrist.x < pinkyMCP.x:
    print("hand pointing to right")
    orientation='right'
  elif wrist.y < thumbMCP.y and wrist.y < pinkyMCP.y:
    print("hand pointing to Down")
    orientation = 'down'
  elif wrist.x > thumbMCP.x and wrist.x > pinkyMCP.x:
    print("hand pointing to left")
    orientation = 'left'
  elif wrist.y > thumbMCP.y and wrist.y > pinkyMCP.y:
    print("hand pointing to up")
    orientation = 'up'
  else:
    orientation = 0


  #Detecting how many finger are down

  if side == 'Left':
    if orientation == 'up':
      fingersDown = MCPY < fingerTipY
      if thumbTip.x < thumbMCP.x:
        fingersDown = np.append(fingersDown,True)
    elif orientation == 'down':
      fingersDown = MCPY > fingerTipY
      if thumbTip.x > thumbMCP.x:
        fingersDown = np.append(fingersDown,True)
    elif orientation == 'right':
      fingersDown = MCPX > fingerTipX
      if thumbTip.y < thumbMCP.y:
        fingersDown=np.append(fingersDown,True)
    elif orientation== 'left':
      fingersDown = MCPX < fingerTipX
      if thumbTip.y > thumbMCP.y:
        fingersDown=np.append(fingersDown,True)

  if side == 'Right':
    if orientation == 'up':
      fingersDown = MCPY < fingerTipY
      if thumbTip.x > thumbMCP.x:
        fingersDown = np.append(fingersDown,True)
    elif orientation == 'down':
      fingersDown = MCPY > fingerTipY
      if thumbTip.x < thumbMCP.x:
        fingersDown = np.append(fingersDown,True)
    elif orientation == 'right':
      fingersDown = MCPX > fingerTipX
      if thumbTip.y > thumbMCP.y:
        fingersDown=np.append(fingersDown,True)
    elif orientation== 'left':
      fingersDown = MCPX < fingerTipX
      if thumbTip.y < thumbMCP.y:
        fingersDown=np.append(fingersDown,True)
  if len(fingersDown) == 4:
    fingersDown = np.append(fingersDown, False)

  fingersDown=5-sum(fingersDown)

  return fingersDown