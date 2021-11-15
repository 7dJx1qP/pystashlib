import sys


# Log messages sent from a plugin instance are transmitted via stderr and are
# encoded with a prefix consisting of special character SOH, then the log
# level (one of t, d, i, w, e, or p - corresponding to trace, debug, info,
# warning, error and progress levels respectively), then special character
# STX.
#
# The LogTrace, LogDebug, LogInfo, LogWarning, and LogError methods, and their equivalent
# formatted methods are intended for use by plugin instances to transmit log
# messages. The LogProgress method is also intended for sending progress data.
#

def __prefix(level_char):
	start_level_char = b'\x01'
	end_level_char = b'\x02'

	ret = start_level_char + level_char + end_level_char
	return ret.decode()


def log(level_char, s):
	if level_char == "":
		return

	print(__prefix(level_char) + s + "\n", file=sys.stderr, flush=True)


def LogTrace(s):
	log(b't', s)


def LogDebug(s):
	log(b'd', s)


def LogInfo(s):
	log(b'i', s)


def LogWarning(s):
	log(b'w', s)


def LogError(s):
	log(b'e', s)


def LogProgress(p):
	progress = min(max(0, p), 1)
	log(b'p', str(progress))