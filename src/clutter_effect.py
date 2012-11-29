import sys
from gi.repository import Clutter

if __name__ == "__main__":
  Clutter.init(sys.argv)
  stage = Clutter.Stage.get_default()
  stage.set_fullscreen(True)
  red = Clutter.Color()
  red.from_string("red")
  stage.set_color(red)
  stage.show()
  stage.connect("button-press-event", lambda s, w: Clutter.main_quit())
  Clutter.main()
  print "Done!"