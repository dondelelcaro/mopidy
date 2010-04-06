import unittest

from mopidy.mpd import MpdAckError, MpdNotImplemented

class MpdExceptionsTest(unittest.TestCase):
    def test_key_error_wrapped_in_mpd_ack_error(self):
        try:
            try:
                raise KeyError(u'Track X not found')
            except KeyError as e:
                raise MpdAckError(e[0])
        except MpdAckError as e:
            self.assertEqual(e.message, u'Track X not found')

    def test_mpd_not_implemented_is_a_mpd_ack_error(self):
        try:
            raise MpdNotImplemented
        except MpdAckError as e:
            self.assertEqual(e.message, u'Not implemented')