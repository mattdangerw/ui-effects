import sys
from gi.repository import Gtk, Gdk, GtkClutter, Clutter 

clutter = Clutter

clutter.init(sys.argv)

stage = clutter.Stage()
stage.set_size(400, 400)

label = clutter.Text()
label.set_editable(False)
label.set_text("Clutter Label Text")
print "Using Clutter version: %s" % Clutter.VERSION_S
color = clutter.Color()
color.from_string("brown")  
label.set_color(color)
# If no position is given it defaults to the upper most left corner.
stage.add_child(label)
stage.show_all()
stage.connect('destroy', lambda w: clutter.main_quit())

clutter.main()