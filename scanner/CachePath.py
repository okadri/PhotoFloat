import os.path
from datetime import datetime
import time

START_TIME = datetime.now()

def message(category, text):
	global START_TIME
	if message.level <= 0:
		sep = "  "
	else:
		sep = "--"
	
	c = datetime.now()-START_TIME
	elapsed = "%02dh%02dm%02ds" % (c.seconds/3600, (c.seconds%3600)/60, c.seconds)
	print "%s %s%s[%s]%s%s" % (elapsed, max(0, message.level) * "  |", sep, category, max(1, (14 - len(category))) * " ", text)
message.level = -1
def next_level():
	message.level += 1
def back_level():
	message.level -= 1
def set_cache_path_base(base):
	trim_base.base = base
def untrim_base(path):
	return os.path.join(trim_base.base, path)
def trim_base_custom(path, base):
	if path.startswith(base):
		path = path[len(base):]
	if path.startswith('/'):
		path = path[1:]
	return path
def trim_base(path):
	return trim_base_custom(path, trim_base.base)
def cache_base(path):
	path = trim_base(path)
	return path
def json_cache(path):
	p = cache_base(path)
	if len(p) == 0:
		return "_root.json"
	return cache_base(path) + "/_" + os.path.basename(path) + ".json"
def image_cache(path, size, square=False):
	assert len(size) == 2
	if square:
		assert size[0] == size[1]
		suffix = size[0] + "s"
	else:
		suffix = "%dx%d" % size
	return cache_base(path) + "_" + suffix + ".jpg"
def file_mtime(path):
	return datetime.fromtimestamp(int(os.path.getmtime(path)))
