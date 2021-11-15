from enum import IntEnum
from . import log

class LogLevel(IntEnum):
	TRACE = 1
	DEBUG = 2
	INFO = 3
	WARN = 4
	ERROR = 5

class Logger:

	_prefixes = {
		b't': '[TRACE]',
		b'd': '[DEBUG]',
		b'i': '[INFO]',
		b'w': '[WARN]',
		b'e': '[ERROR]',
	}

	def __init__(self, log_level=LogLevel.TRACE, plugin=True):
		self.log_level = log_level
		self.plugin = plugin

	def _log(self, level_char, s):
		if self.plugin:
			log.log(level_char, s)
		else:
			print(self._prefixes[level_char], s)

	def LogTrace(self, s):
		if self.log_level <= LogLevel.TRACE:
			self._log(b't', s)


	def LogDebug(self, s):
		if self.log_level <= LogLevel.DEBUG:
			self._log(b'd', s)


	def LogInfo(self, s):
		if self.log_level <= LogLevel.INFO:
			self._log(b'i', s)


	def LogWarning(self, s):
		if self.log_level <= LogLevel.WARN:
			self._log(b'w', s)


	def LogError(self, s):
		if self.log_level <= LogLevel.ERROR:
			self._log(b'e', s)


	def LogProgress(self, p):
		if self.plugin:
			progress = min(max(0, p), 1)
			self._log(b'p', str(progress))

logger = Logger()