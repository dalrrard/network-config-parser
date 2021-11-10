# Generated from /home/user/Projects/network-config-parser/ncp/parser/IOSGrammar.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0085")
        buf.write("\u0124\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\3\2\7\2_\n\2\f\2\16\2b\13\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\6\3j\n\3\r\3\16\3k\3\3\3\3\3\4\3\4\5\4r\n\4\3\4\5\4u")
        buf.write("\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u009d")
        buf.write("\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u00a9")
        buf.write("\n\b\3\b\3\b\3\b\5\b\u00ae\n\b\3\b\5\b\u00b1\n\b\5\b\u00b3")
        buf.write("\n\b\3\b\3\b\5\b\u00b7\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\5\f\u00c3\n\f\3\f\3\f\5\f\u00c7\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\5\r\u00cf\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\5\23\u00e4\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u00f0\n\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\2\2/\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\2\4\3\2\16\20\4\2\25\25qq\2\u012f\2`\3\2")
        buf.write("\2\2\4f\3\2\2\2\6t\3\2\2\2\b\u009c\3\2\2\2\n\u009e\3\2")
        buf.write("\2\2\f\u00a1\3\2\2\2\16\u00a4\3\2\2\2\20\u00b8\3\2\2\2")
        buf.write("\22\u00ba\3\2\2\2\24\u00bc\3\2\2\2\26\u00bf\3\2\2\2\30")
        buf.write("\u00c8\3\2\2\2\32\u00d0\3\2\2\2\34\u00d6\3\2\2\2\36\u00d8")
        buf.write("\3\2\2\2 \u00da\3\2\2\2\"\u00dc\3\2\2\2$\u00df\3\2\2\2")
        buf.write("&\u00e5\3\2\2\2(\u00ea\3\2\2\2*\u00f1\3\2\2\2,\u00f3\3")
        buf.write("\2\2\2.\u00f5\3\2\2\2\60\u00f7\3\2\2\2\62\u00f9\3\2\2")
        buf.write("\2\64\u00fb\3\2\2\2\66\u00fd\3\2\2\28\u00ff\3\2\2\2:\u0101")
        buf.write("\3\2\2\2<\u0103\3\2\2\2>\u0105\3\2\2\2@\u0107\3\2\2\2")
        buf.write("B\u0109\3\2\2\2D\u010b\3\2\2\2F\u010d\3\2\2\2H\u010f\3")
        buf.write("\2\2\2J\u0111\3\2\2\2L\u0113\3\2\2\2N\u0115\3\2\2\2P\u0117")
        buf.write("\3\2\2\2R\u0119\3\2\2\2T\u011b\3\2\2\2V\u011d\3\2\2\2")
        buf.write("X\u011f\3\2\2\2Z\u0121\3\2\2\2\\_\7\177\2\2]_\5\6\4\2")
        buf.write("^\\\3\2\2\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ac")
        buf.write("\3\2\2\2b`\3\2\2\2cd\7&\2\2de\7\2\2\3e\3\3\2\2\2fg\7\177")
        buf.write("\2\2gi\7\u0084\2\2hj\5\6\4\2ih\3\2\2\2jk\3\2\2\2ki\3\2")
        buf.write("\2\2kl\3\2\2\2lm\3\2\2\2mn\7\u0085\2\2n\5\3\2\2\2ou\7")
        buf.write("\5\2\2pr\7\6\2\2qp\3\2\2\2qr\3\2\2\2rs\3\2\2\2su\5\b\5")
        buf.write("\2to\3\2\2\2tq\3\2\2\2uv\3\2\2\2vw\7\177\2\2w\7\3\2\2")
        buf.write("\2x\u009d\5\n\6\2y\u009d\5\f\7\2z\u009d\5\16\b\2{\u009d")
        buf.write("\5\20\t\2|\u009d\5\22\n\2}\u009d\5\24\13\2~\u009d\5\26")
        buf.write("\f\2\177\u009d\5\30\r\2\u0080\u009d\5$\23\2\u0081\u009d")
        buf.write("\5&\24\2\u0082\u009d\5(\25\2\u0083\u009d\5*\26\2\u0084")
        buf.write("\u009d\5,\27\2\u0085\u009d\5.\30\2\u0086\u009d\5\60\31")
        buf.write("\2\u0087\u009d\5\62\32\2\u0088\u009d\5\64\33\2\u0089\u009d")
        buf.write("\5\66\34\2\u008a\u009d\58\35\2\u008b\u009d\5:\36\2\u008c")
        buf.write("\u009d\5<\37\2\u008d\u009d\5> \2\u008e\u009d\5@!\2\u008f")
        buf.write("\u009d\5B\"\2\u0090\u009d\5D#\2\u0091\u009d\5F$\2\u0092")
        buf.write("\u009d\5H%\2\u0093\u009d\5J&\2\u0094\u009d\5L\'\2\u0095")
        buf.write("\u009d\5N(\2\u0096\u009d\5P)\2\u0097\u009d\5R*\2\u0098")
        buf.write("\u009d\5T+\2\u0099\u009d\5V,\2\u009a\u009d\5X-\2\u009b")
        buf.write("\u009d\5Z.\2\u009cx\3\2\2\2\u009cy\3\2\2\2\u009cz\3\2")
        buf.write("\2\2\u009c{\3\2\2\2\u009c|\3\2\2\2\u009c}\3\2\2\2\u009c")
        buf.write("~\3\2\2\2\u009c\177\3\2\2\2\u009c\u0080\3\2\2\2\u009c")
        buf.write("\u0081\3\2\2\2\u009c\u0082\3\2\2\2\u009c\u0083\3\2\2\2")
        buf.write("\u009c\u0084\3\2\2\2\u009c\u0085\3\2\2\2\u009c\u0086\3")
        buf.write("\2\2\2\u009c\u0087\3\2\2\2\u009c\u0088\3\2\2\2\u009c\u0089")
        buf.write("\3\2\2\2\u009c\u008a\3\2\2\2\u009c\u008b\3\2\2\2\u009c")
        buf.write("\u008c\3\2\2\2\u009c\u008d\3\2\2\2\u009c\u008e\3\2\2\2")
        buf.write("\u009c\u008f\3\2\2\2\u009c\u0090\3\2\2\2\u009c\u0091\3")
        buf.write("\2\2\2\u009c\u0092\3\2\2\2\u009c\u0093\3\2\2\2\u009c\u0094")
        buf.write("\3\2\2\2\u009c\u0095\3\2\2\2\u009c\u0096\3\2\2\2\u009c")
        buf.write("\u0097\3\2\2\2\u009c\u0098\3\2\2\2\u009c\u0099\3\2\2\2")
        buf.write("\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2\u009d\t\3\2\2")
        buf.write("\2\u009e\u009f\7)\2\2\u009f\u00a0\7\u0080\2\2\u00a0\13")
        buf.write("\3\2\2\2\u00a1\u00a2\7 \2\2\u00a2\u00a3\7\u0080\2\2\u00a3")
        buf.write("\r\3\2\2\2\u00a4\u00b6\7\7\2\2\u00a5\u00b7\7\b\2\2\u00a6")
        buf.write("\u00a8\7\t\2\2\u00a7\u00a9\7\n\2\2\u00a8\u00a7\3\2\2\2")
        buf.write("\u00a8\u00a9\3\2\2\2\u00a9\u00b2\3\2\2\2\u00aa\u00b3\7")
        buf.write("\13\2\2\u00ab\u00ad\7\f\2\2\u00ac\u00ae\7\r\2\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2")
        buf.write("\u00af\u00b1\t\2\2\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3")
        buf.write("\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00aa\3\2\2\2\u00b2\u00ab")
        buf.write("\3\2\2\2\u00b3\u00b7\3\2\2\2\u00b4\u00b7\7\21\2\2\u00b5")
        buf.write("\u00b7\7\22\2\2\u00b6\u00a5\3\2\2\2\u00b6\u00a6\3\2\2")
        buf.write("\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\17\3")
        buf.write("\2\2\2\u00b8\u00b9\t\3\2\2\u00b9\21\3\2\2\2\u00ba\u00bb")
        buf.write("\7s\2\2\u00bb\23\3\2\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7l\2\2\u00be\25\3\2\2\2\u00bf\u00c0\7\\\2\2\u00c0\u00c2")
        buf.write("\7\u0080\2\2\u00c1\u00c3\7]\2\2\u00c2\u00c1\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6\7l\2\2")
        buf.write("\u00c5\u00c7\7\u0080\2\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\27\3\2\2\2\u00c8\u00ce\7O\2\2\u00c9\u00cf")
        buf.write("\7Q\2\2\u00ca\u00cf\5\32\16\2\u00cb\u00cf\5\34\17\2\u00cc")
        buf.write("\u00cf\5\36\20\2\u00cd\u00cf\5 \21\2\u00ce\u00c9\3\2\2")
        buf.write("\2\u00ce\u00ca\3\2\2\2\u00ce\u00cb\3\2\2\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\31\3\2\2\2\u00d0\u00d1")
        buf.write("\7P\2\2\u00d1\u00d2\7H\2\2\u00d2\u00d3\7\3\2\2\u00d3\u00d4")
        buf.write("\7\u0080\2\2\u00d4\u00d5\5\4\3\2\u00d5\33\3\2\2\2\u00d6")
        buf.write("\u00d7\7R\2\2\u00d7\35\3\2\2\2\u00d8\u00d9\7S\2\2\u00d9")
        buf.write("\37\3\2\2\2\u00da\u00db\7T\2\2\u00db!\3\2\2\2\u00dc\u00dd")
        buf.write("\7w\2\2\u00dd\u00de\5$\23\2\u00de#\3\2\2\2\u00df\u00e3")
        buf.write("\7H\2\2\u00e0\u00e4\7\u0080\2\2\u00e1\u00e2\7+\2\2\u00e2")
        buf.write("\u00e4\7\u0080\2\2\u00e3\u00e0\3\2\2\2\u00e3\u00e1\3\2")
        buf.write("\2\2\u00e3\u00e4\3\2\2\2\u00e4%\3\2\2\2\u00e5\u00e6\7")
        buf.write("m\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8\7U\2\2\u00e8\u00e9")
        buf.write("\7\u0080\2\2\u00e9\'\3\2\2\2\u00ea\u00ef\7\66\2\2\u00eb")
        buf.write("\u00ec\78\2\2\u00ec\u00f0\79\2\2\u00ed\u00f0\7:\2\2\u00ee")
        buf.write("\u00f0\7;\2\2\u00ef\u00eb\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00ef\u00ee\3\2\2\2\u00f0)\3\2\2\2\u00f1\u00f2\7n\2\2")
        buf.write("\u00f2+\3\2\2\2\u00f3\u00f4\7V\2\2\u00f4-\3\2\2\2\u00f5")
        buf.write("\u00f6\7b\2\2\u00f6/\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8")
        buf.write("\61\3\2\2\2\u00f9\u00fa\7*\2\2\u00fa\63\3\2\2\2\u00fb")
        buf.write("\u00fc\7Z\2\2\u00fc\65\3\2\2\2\u00fd\u00fe\7<\2\2\u00fe")
        buf.write("\67\3\2\2\2\u00ff\u0100\7z\2\2\u01009\3\2\2\2\u0101\u0102")
        buf.write("\7\36\2\2\u0102;\3\2\2\2\u0103\u0104\7f\2\2\u0104=\3\2")
        buf.write("\2\2\u0105\u0106\7`\2\2\u0106?\3\2\2\2\u0107\u0108\7\32")
        buf.write("\2\2\u0108A\3\2\2\2\u0109\u010a\7C\2\2\u010aC\3\2\2\2")
        buf.write("\u010b\u010c\7-\2\2\u010cE\3\2\2\2\u010d\u010e\7r\2\2")
        buf.write("\u010eG\3\2\2\2\u010f\u0110\7p\2\2\u0110I\3\2\2\2\u0111")
        buf.write("\u0112\7\37\2\2\u0112K\3\2\2\2\u0113\u0114\7\'\2\2\u0114")
        buf.write("M\3\2\2\2\u0115\u0116\7\34\2\2\u0116O\3\2\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118Q\3\2\2\2\u0119\u011a\7w\2\2\u011aS\3\2\2")
        buf.write("\2\u011b\u011c\7~\2\2\u011cU\3\2\2\2\u011d\u011e\7\23")
        buf.write("\2\2\u011eW\3\2\2\2\u011f\u0120\7t\2\2\u0120Y\3\2\2\2")
        buf.write("\u0121\u0122\7\27\2\2\u0122[\3\2\2\2\22^`kqt\u009c\u00a8")
        buf.write("\u00ad\u00b0\u00b2\u00b6\u00c2\u00c6\u00ce\u00e3\u00ef")
        return buf.getvalue()


class IOSGrammarParser ( Parser ):

    grammarFileName = "IOSGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'tacacs+'", "<INVALID>", "'!'", "'no'", 
                     "'service'", "'pad'", "'timestamps'", "<INVALID>", 
                     "'uptime'", "'datetime'", "'msec'", "'localtime'", 
                     "'show-timezone'", "'year'", "'password-encryption'", 
                     "'unsupported-transceiver'", "'banner'", "'priority-queue'", 
                     "'boot-start-marker'", "'path'", "'ntp'", "'subject-name'", 
                     "'fqdn'", "'vlan'", "'af-interface'", "'snmp-server'", 
                     "'permit'", "'port-channel'", "'access-list'", "'hostname'", 
                     "'mtu'", "'revocation-check'", "'time-period'", "'icmp-echo'", 
                     "'service-family'", "'end'", "'arp'", "'storm-control'", 
                     "'version'", "'mls'", "'name'", "'auto'", "'class-map'", 
                     "'private-vlan'", "'channel-protocol'", "'address-family'", 
                     "'frequency'", "'switchport'", "'match'", "'rollback'", 
                     "'hidekeys'", "'clock'", "'read-calendar'", "'summer-time'", 
                     "<INVALID>", "'timezone'", "'update-calendar'", "'crypto'", 
                     "'action'", "'ipv6'", "'tacacs-server'", "'exit-address-family'", 
                     "'srr-queue'", "'state'", "'track'", "'topology'", 
                     "'police'", "'enrollment'", "'address'", "'server'", 
                     "'set'", "'eigrp'", "'timeout'", "'description'", "'write-memory'", 
                     "'router'", "'aaa'", "'group'", "'new-model'", "'authentication'", 
                     "'authorization'", "'accounting'", "'source-interface'", 
                     "'vtp'", "'length'", "'channel-group'", "'key-string'", 
                     "'key'", "'certificate'", "'username'", "<INVALID>", 
                     "'exit-af-interface'", "'deny'", "'spanning-tree'", 
                     "'shutdown'", "'login'", "'exit-af-topology'", "'service-policy'", 
                     "'quit'", "'archive'", "'exit-service-family'", "'notify'", 
                     "'network'", "'record'", "'enable'", "<INVALID>", "'ip'", 
                     "'system'", "'queue-set'", "'interface'", "'boot-end-marker'", 
                     "'policy-map'", "'logging'", "'line'", "'passive-interface'", 
                     "'exec-timeout'", "'tacacs'", "'exit-sf-topology'", 
                     "'class'", "'errdisable'", "'vpdn'", "'bridge'", "'radius-server'", 
                     "'vstack'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IGNORE", "EXCLAMATION", 
                      "NO", "SERVICE", "PAD", "TIMESTAMPS", "LOG_LEVEL", 
                      "UPTIME", "DATETIME", "MSEC", "LOCALTIME", "SHOW_TIMEZONE", 
                      "YEAR", "PASSWORD_ENCRYPTION", "UNSUPPORTED_TRANSCEIVER", 
                      "BANNER", "PRIORITY_QUEUE", "BOOT_START_MARKER", "PATH", 
                      "NTP", "SUBJECT_NAME", "FQDN", "VLAN", "AF_INTERFACE", 
                      "SNMP_SERVER", "PERMIT", "PORT_CHANNEL", "ACCESS_LIST", 
                      "HOSTNAME", "MTU", "REVOCATION_CHECK", "TIME_PERIOD", 
                      "ICMP_ECHO", "SERVICE_FAMILY", "END", "ARP", "STORM_CONTROL", 
                      "VERSION", "MLS", "NAME", "AUTO", "CLASS_MAP", "PRIVATE_VLAN", 
                      "CHANNEL_PROTOCOL", "ADDRESS_FAMILY", "FREQUENCY", 
                      "SWITCHPORT", "MATCH", "ROLLBACK", "HIDEKEYS", "CLOCK", 
                      "READ_CALENDAR", "SUMMER_TIME", "ZONE", "TIMEZONE", 
                      "UPDATE_CALENDAR", "CRYPTO", "ACTION", "IPV6", "TACACS_SERVER", 
                      "EXIT_ADDRESS_FAMILY", "SRR_QUEUE", "STATE", "TRACK", 
                      "TOPOLOGY", "POLICE", "ENROLLMENT", "ADDRESS", "SERVER", 
                      "SET", "EIGRP", "TIMEOUT", "DESCRIPTION", "WRITE_MEMORY", 
                      "ROUTER", "AAA", "GROUP", "NEW_MODEL", "AUTHENTICATION", 
                      "AUTHORIZATION", "ACCOUNTING", "SOURCE_INTERFACE", 
                      "VTP", "LENGTH", "CHANNEL_GROUP", "KEY_STRING", "KEY", 
                      "CERTIFICATE", "USERNAME", "PRIVILEGE", "EXIT_AF_INTERFACE", 
                      "DENY", "SPANNING_TREE", "SHUTDOWN", "LOGIN", "EXIT_AF_TOPOLOGY", 
                      "SERVICE_POLICY", "QUIT", "ARCHIVE", "EXIT_SERVICE_FAMILY", 
                      "NOTIFY", "NETWORK", "RECORD", "ENABLE", "CREDENTIAL_TYPE", 
                      "IP", "SYSTEM", "QUEUE_SET", "INTERFACE", "BOOT_END_MARKER", 
                      "POLICY_MAP", "LOGGING", "LINE", "PASSIVE_INTERFACE", 
                      "EXEC_TIMEOUT", "TACACS", "EXIT_SF_TOPOLOGY", "CLASS", 
                      "ERRDISABLE", "VPDN", "BRIDGE", "RADIUS_SERVER", "VSTACK", 
                      "NEWLINE", "ID", "WORD", "IPV4", "INT", "INDENT", 
                      "DEDENT" ]

    RULE_config = 0
    RULE_suite = 1
    RULE_stmt = 2
    RULE_command = 3
    RULE_version_stmt = 4
    RULE_hostname_stmt = 5
    RULE_service_stmt = 6
    RULE_boot_stmt = 7
    RULE_logging_stmt = 8
    RULE_enable_stmt = 9
    RULE_username_stmt = 10
    RULE_aaa_stmt = 11
    RULE_aaa_group = 12
    RULE_aaa_authentication = 13
    RULE_aaa_authorization = 14
    RULE_aaa_accounting = 15
    RULE_tacacs = 16
    RULE_server_stmt = 17
    RULE_ip_stmt = 18
    RULE_clock_stmt = 19
    RULE_system_stmt = 20
    RULE_vtp_stmt = 21
    RULE_login_stmt = 22
    RULE_ipv6_stmt = 23
    RULE_mls_stmt = 24
    RULE_key_stmt = 25
    RULE_crypto_stmt = 26
    RULE_errdisable_stmt = 27
    RULE_port_channel_stmt = 28
    RULE_archive_stmt = 29
    RULE_spanning_tree_stmt = 30
    RULE_vlan_stmt = 31
    RULE_track_stmt = 32
    RULE_class_map_stmt = 33
    RULE_policy_map_stmt = 34
    RULE_interface_stmt = 35
    RULE_access_list_stmt = 36
    RULE_arp_stmt = 37
    RULE_snmp_server_stmt = 38
    RULE_tacacs_server_stmt = 39
    RULE_tacacs_stmt = 40
    RULE_vstack_stmt = 41
    RULE_banner_stmt = 42
    RULE_line_stmt = 43
    RULE_ntp_stmt = 44

    ruleNames =  [ "config", "suite", "stmt", "command", "version_stmt", 
                   "hostname_stmt", "service_stmt", "boot_stmt", "logging_stmt", 
                   "enable_stmt", "username_stmt", "aaa_stmt", "aaa_group", 
                   "aaa_authentication", "aaa_authorization", "aaa_accounting", 
                   "tacacs", "server_stmt", "ip_stmt", "clock_stmt", "system_stmt", 
                   "vtp_stmt", "login_stmt", "ipv6_stmt", "mls_stmt", "key_stmt", 
                   "crypto_stmt", "errdisable_stmt", "port_channel_stmt", 
                   "archive_stmt", "spanning_tree_stmt", "vlan_stmt", "track_stmt", 
                   "class_map_stmt", "policy_map_stmt", "interface_stmt", 
                   "access_list_stmt", "arp_stmt", "snmp_server_stmt", "tacacs_server_stmt", 
                   "tacacs_stmt", "vstack_stmt", "banner_stmt", "line_stmt", 
                   "ntp_stmt" ]

    EOF = Token.EOF
    T__0=1
    IGNORE=2
    EXCLAMATION=3
    NO=4
    SERVICE=5
    PAD=6
    TIMESTAMPS=7
    LOG_LEVEL=8
    UPTIME=9
    DATETIME=10
    MSEC=11
    LOCALTIME=12
    SHOW_TIMEZONE=13
    YEAR=14
    PASSWORD_ENCRYPTION=15
    UNSUPPORTED_TRANSCEIVER=16
    BANNER=17
    PRIORITY_QUEUE=18
    BOOT_START_MARKER=19
    PATH=20
    NTP=21
    SUBJECT_NAME=22
    FQDN=23
    VLAN=24
    AF_INTERFACE=25
    SNMP_SERVER=26
    PERMIT=27
    PORT_CHANNEL=28
    ACCESS_LIST=29
    HOSTNAME=30
    MTU=31
    REVOCATION_CHECK=32
    TIME_PERIOD=33
    ICMP_ECHO=34
    SERVICE_FAMILY=35
    END=36
    ARP=37
    STORM_CONTROL=38
    VERSION=39
    MLS=40
    NAME=41
    AUTO=42
    CLASS_MAP=43
    PRIVATE_VLAN=44
    CHANNEL_PROTOCOL=45
    ADDRESS_FAMILY=46
    FREQUENCY=47
    SWITCHPORT=48
    MATCH=49
    ROLLBACK=50
    HIDEKEYS=51
    CLOCK=52
    READ_CALENDAR=53
    SUMMER_TIME=54
    ZONE=55
    TIMEZONE=56
    UPDATE_CALENDAR=57
    CRYPTO=58
    ACTION=59
    IPV6=60
    TACACS_SERVER=61
    EXIT_ADDRESS_FAMILY=62
    SRR_QUEUE=63
    STATE=64
    TRACK=65
    TOPOLOGY=66
    POLICE=67
    ENROLLMENT=68
    ADDRESS=69
    SERVER=70
    SET=71
    EIGRP=72
    TIMEOUT=73
    DESCRIPTION=74
    WRITE_MEMORY=75
    ROUTER=76
    AAA=77
    GROUP=78
    NEW_MODEL=79
    AUTHENTICATION=80
    AUTHORIZATION=81
    ACCOUNTING=82
    SOURCE_INTERFACE=83
    VTP=84
    LENGTH=85
    CHANNEL_GROUP=86
    KEY_STRING=87
    KEY=88
    CERTIFICATE=89
    USERNAME=90
    PRIVILEGE=91
    EXIT_AF_INTERFACE=92
    DENY=93
    SPANNING_TREE=94
    SHUTDOWN=95
    LOGIN=96
    EXIT_AF_TOPOLOGY=97
    SERVICE_POLICY=98
    QUIT=99
    ARCHIVE=100
    EXIT_SERVICE_FAMILY=101
    NOTIFY=102
    NETWORK=103
    RECORD=104
    ENABLE=105
    CREDENTIAL_TYPE=106
    IP=107
    SYSTEM=108
    QUEUE_SET=109
    INTERFACE=110
    BOOT_END_MARKER=111
    POLICY_MAP=112
    LOGGING=113
    LINE=114
    PASSIVE_INTERFACE=115
    EXEC_TIMEOUT=116
    TACACS=117
    EXIT_SF_TOPOLOGY=118
    CLASS=119
    ERRDISABLE=120
    VPDN=121
    BRIDGE=122
    RADIUS_SERVER=123
    VSTACK=124
    NEWLINE=125
    ID=126
    WORD=127
    IPV4=128
    INT=129
    INDENT=130
    DEDENT=131

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ConfigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(IOSGrammarParser.END, 0)

        def EOF(self):
            return self.getToken(IOSGrammarParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(IOSGrammarParser.NEWLINE)
            else:
                return self.getToken(IOSGrammarParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOSGrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(IOSGrammarParser.StmtContext,i)


        def getRuleIndex(self):
            return IOSGrammarParser.RULE_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig" ):
                listener.enterConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig" ):
                listener.exitConfig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfig" ):
                return visitor.visitConfig(self)
            else:
                return visitor.visitChildren(self)




    def config(self):

        localctx = IOSGrammarParser.ConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IOSGrammarParser.EXCLAMATION) | (1 << IOSGrammarParser.NO) | (1 << IOSGrammarParser.SERVICE) | (1 << IOSGrammarParser.BANNER) | (1 << IOSGrammarParser.BOOT_START_MARKER) | (1 << IOSGrammarParser.NTP) | (1 << IOSGrammarParser.VLAN) | (1 << IOSGrammarParser.SNMP_SERVER) | (1 << IOSGrammarParser.PORT_CHANNEL) | (1 << IOSGrammarParser.ACCESS_LIST) | (1 << IOSGrammarParser.HOSTNAME) | (1 << IOSGrammarParser.ARP) | (1 << IOSGrammarParser.VERSION) | (1 << IOSGrammarParser.MLS) | (1 << IOSGrammarParser.CLASS_MAP) | (1 << IOSGrammarParser.CLOCK) | (1 << IOSGrammarParser.CRYPTO) | (1 << IOSGrammarParser.IPV6) | (1 << IOSGrammarParser.TACACS_SERVER))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (IOSGrammarParser.TRACK - 65)) | (1 << (IOSGrammarParser.SERVER - 65)) | (1 << (IOSGrammarParser.AAA - 65)) | (1 << (IOSGrammarParser.VTP - 65)) | (1 << (IOSGrammarParser.KEY - 65)) | (1 << (IOSGrammarParser.USERNAME - 65)) | (1 << (IOSGrammarParser.SPANNING_TREE - 65)) | (1 << (IOSGrammarParser.LOGIN - 65)) | (1 << (IOSGrammarParser.ARCHIVE - 65)) | (1 << (IOSGrammarParser.ENABLE - 65)) | (1 << (IOSGrammarParser.IP - 65)) | (1 << (IOSGrammarParser.SYSTEM - 65)) | (1 << (IOSGrammarParser.INTERFACE - 65)) | (1 << (IOSGrammarParser.BOOT_END_MARKER - 65)) | (1 << (IOSGrammarParser.POLICY_MAP - 65)) | (1 << (IOSGrammarParser.LOGGING - 65)) | (1 << (IOSGrammarParser.LINE - 65)) | (1 << (IOSGrammarParser.TACACS - 65)) | (1 << (IOSGrammarParser.ERRDISABLE - 65)) | (1 << (IOSGrammarParser.VSTACK - 65)) | (1 << (IOSGrammarParser.NEWLINE - 65)))) != 0):
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [IOSGrammarParser.NEWLINE]:
                    self.state = 90
                    self.match(IOSGrammarParser.NEWLINE)
                    pass
                elif token in [IOSGrammarParser.EXCLAMATION, IOSGrammarParser.NO, IOSGrammarParser.SERVICE, IOSGrammarParser.BANNER, IOSGrammarParser.BOOT_START_MARKER, IOSGrammarParser.NTP, IOSGrammarParser.VLAN, IOSGrammarParser.SNMP_SERVER, IOSGrammarParser.PORT_CHANNEL, IOSGrammarParser.ACCESS_LIST, IOSGrammarParser.HOSTNAME, IOSGrammarParser.ARP, IOSGrammarParser.VERSION, IOSGrammarParser.MLS, IOSGrammarParser.CLASS_MAP, IOSGrammarParser.CLOCK, IOSGrammarParser.CRYPTO, IOSGrammarParser.IPV6, IOSGrammarParser.TACACS_SERVER, IOSGrammarParser.TRACK, IOSGrammarParser.SERVER, IOSGrammarParser.AAA, IOSGrammarParser.VTP, IOSGrammarParser.KEY, IOSGrammarParser.USERNAME, IOSGrammarParser.SPANNING_TREE, IOSGrammarParser.LOGIN, IOSGrammarParser.ARCHIVE, IOSGrammarParser.ENABLE, IOSGrammarParser.IP, IOSGrammarParser.SYSTEM, IOSGrammarParser.INTERFACE, IOSGrammarParser.BOOT_END_MARKER, IOSGrammarParser.POLICY_MAP, IOSGrammarParser.LOGGING, IOSGrammarParser.LINE, IOSGrammarParser.TACACS, IOSGrammarParser.ERRDISABLE, IOSGrammarParser.VSTACK]:
                    self.state = 91
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(IOSGrammarParser.END)
            self.state = 98
            self.match(IOSGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuiteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(IOSGrammarParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(IOSGrammarParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(IOSGrammarParser.DEDENT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOSGrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(IOSGrammarParser.StmtContext,i)


        def getRuleIndex(self):
            return IOSGrammarParser.RULE_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuite" ):
                listener.enterSuite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuite" ):
                listener.exitSuite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuite" ):
                return visitor.visitSuite(self)
            else:
                return visitor.visitChildren(self)




    def suite(self):

        localctx = IOSGrammarParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(IOSGrammarParser.NEWLINE)
            self.state = 101
            self.match(IOSGrammarParser.INDENT)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.stmt()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IOSGrammarParser.EXCLAMATION) | (1 << IOSGrammarParser.NO) | (1 << IOSGrammarParser.SERVICE) | (1 << IOSGrammarParser.BANNER) | (1 << IOSGrammarParser.BOOT_START_MARKER) | (1 << IOSGrammarParser.NTP) | (1 << IOSGrammarParser.VLAN) | (1 << IOSGrammarParser.SNMP_SERVER) | (1 << IOSGrammarParser.PORT_CHANNEL) | (1 << IOSGrammarParser.ACCESS_LIST) | (1 << IOSGrammarParser.HOSTNAME) | (1 << IOSGrammarParser.ARP) | (1 << IOSGrammarParser.VERSION) | (1 << IOSGrammarParser.MLS) | (1 << IOSGrammarParser.CLASS_MAP) | (1 << IOSGrammarParser.CLOCK) | (1 << IOSGrammarParser.CRYPTO) | (1 << IOSGrammarParser.IPV6) | (1 << IOSGrammarParser.TACACS_SERVER))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (IOSGrammarParser.TRACK - 65)) | (1 << (IOSGrammarParser.SERVER - 65)) | (1 << (IOSGrammarParser.AAA - 65)) | (1 << (IOSGrammarParser.VTP - 65)) | (1 << (IOSGrammarParser.KEY - 65)) | (1 << (IOSGrammarParser.USERNAME - 65)) | (1 << (IOSGrammarParser.SPANNING_TREE - 65)) | (1 << (IOSGrammarParser.LOGIN - 65)) | (1 << (IOSGrammarParser.ARCHIVE - 65)) | (1 << (IOSGrammarParser.ENABLE - 65)) | (1 << (IOSGrammarParser.IP - 65)) | (1 << (IOSGrammarParser.SYSTEM - 65)) | (1 << (IOSGrammarParser.INTERFACE - 65)) | (1 << (IOSGrammarParser.BOOT_END_MARKER - 65)) | (1 << (IOSGrammarParser.POLICY_MAP - 65)) | (1 << (IOSGrammarParser.LOGGING - 65)) | (1 << (IOSGrammarParser.LINE - 65)) | (1 << (IOSGrammarParser.TACACS - 65)) | (1 << (IOSGrammarParser.ERRDISABLE - 65)) | (1 << (IOSGrammarParser.VSTACK - 65)))) != 0)):
                    break

            self.state = 107
            self.match(IOSGrammarParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(IOSGrammarParser.NEWLINE, 0)

        def EXCLAMATION(self):
            return self.getToken(IOSGrammarParser.EXCLAMATION, 0)

        def command(self):
            return self.getTypedRuleContext(IOSGrammarParser.CommandContext,0)


        def NO(self):
            return self.getToken(IOSGrammarParser.NO, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = IOSGrammarParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IOSGrammarParser.EXCLAMATION]:
                self.state = 109
                self.match(IOSGrammarParser.EXCLAMATION)
                pass
            elif token in [IOSGrammarParser.NO, IOSGrammarParser.SERVICE, IOSGrammarParser.BANNER, IOSGrammarParser.BOOT_START_MARKER, IOSGrammarParser.NTP, IOSGrammarParser.VLAN, IOSGrammarParser.SNMP_SERVER, IOSGrammarParser.PORT_CHANNEL, IOSGrammarParser.ACCESS_LIST, IOSGrammarParser.HOSTNAME, IOSGrammarParser.ARP, IOSGrammarParser.VERSION, IOSGrammarParser.MLS, IOSGrammarParser.CLASS_MAP, IOSGrammarParser.CLOCK, IOSGrammarParser.CRYPTO, IOSGrammarParser.IPV6, IOSGrammarParser.TACACS_SERVER, IOSGrammarParser.TRACK, IOSGrammarParser.SERVER, IOSGrammarParser.AAA, IOSGrammarParser.VTP, IOSGrammarParser.KEY, IOSGrammarParser.USERNAME, IOSGrammarParser.SPANNING_TREE, IOSGrammarParser.LOGIN, IOSGrammarParser.ARCHIVE, IOSGrammarParser.ENABLE, IOSGrammarParser.IP, IOSGrammarParser.SYSTEM, IOSGrammarParser.INTERFACE, IOSGrammarParser.BOOT_END_MARKER, IOSGrammarParser.POLICY_MAP, IOSGrammarParser.LOGGING, IOSGrammarParser.LINE, IOSGrammarParser.TACACS, IOSGrammarParser.ERRDISABLE, IOSGrammarParser.VSTACK]:
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IOSGrammarParser.NO:
                    self.state = 110
                    self.match(IOSGrammarParser.NO)


                self.state = 113
                self.command()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 116
            self.match(IOSGrammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def version_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Version_stmtContext,0)


        def hostname_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Hostname_stmtContext,0)


        def service_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Service_stmtContext,0)


        def boot_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Boot_stmtContext,0)


        def logging_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Logging_stmtContext,0)


        def enable_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Enable_stmtContext,0)


        def username_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Username_stmtContext,0)


        def aaa_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Aaa_stmtContext,0)


        def server_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Server_stmtContext,0)


        def ip_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Ip_stmtContext,0)


        def clock_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Clock_stmtContext,0)


        def system_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.System_stmtContext,0)


        def vtp_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Vtp_stmtContext,0)


        def login_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Login_stmtContext,0)


        def ipv6_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Ipv6_stmtContext,0)


        def mls_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Mls_stmtContext,0)


        def key_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Key_stmtContext,0)


        def crypto_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Crypto_stmtContext,0)


        def errdisable_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Errdisable_stmtContext,0)


        def port_channel_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Port_channel_stmtContext,0)


        def archive_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Archive_stmtContext,0)


        def spanning_tree_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Spanning_tree_stmtContext,0)


        def vlan_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Vlan_stmtContext,0)


        def track_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Track_stmtContext,0)


        def class_map_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Class_map_stmtContext,0)


        def policy_map_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Policy_map_stmtContext,0)


        def interface_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Interface_stmtContext,0)


        def access_list_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Access_list_stmtContext,0)


        def arp_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Arp_stmtContext,0)


        def snmp_server_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Snmp_server_stmtContext,0)


        def tacacs_server_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Tacacs_server_stmtContext,0)


        def tacacs_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Tacacs_stmtContext,0)


        def vstack_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Vstack_stmtContext,0)


        def banner_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Banner_stmtContext,0)


        def line_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Line_stmtContext,0)


        def ntp_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Ntp_stmtContext,0)


        def getRuleIndex(self):
            return IOSGrammarParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = IOSGrammarParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IOSGrammarParser.VERSION]:
                self.state = 118
                self.version_stmt()
                pass
            elif token in [IOSGrammarParser.HOSTNAME]:
                self.state = 119
                self.hostname_stmt()
                pass
            elif token in [IOSGrammarParser.SERVICE]:
                self.state = 120
                self.service_stmt()
                pass
            elif token in [IOSGrammarParser.BOOT_START_MARKER, IOSGrammarParser.BOOT_END_MARKER]:
                self.state = 121
                self.boot_stmt()
                pass
            elif token in [IOSGrammarParser.LOGGING]:
                self.state = 122
                self.logging_stmt()
                pass
            elif token in [IOSGrammarParser.ENABLE]:
                self.state = 123
                self.enable_stmt()
                pass
            elif token in [IOSGrammarParser.USERNAME]:
                self.state = 124
                self.username_stmt()
                pass
            elif token in [IOSGrammarParser.AAA]:
                self.state = 125
                self.aaa_stmt()
                pass
            elif token in [IOSGrammarParser.SERVER]:
                self.state = 126
                self.server_stmt()
                pass
            elif token in [IOSGrammarParser.IP]:
                self.state = 127
                self.ip_stmt()
                pass
            elif token in [IOSGrammarParser.CLOCK]:
                self.state = 128
                self.clock_stmt()
                pass
            elif token in [IOSGrammarParser.SYSTEM]:
                self.state = 129
                self.system_stmt()
                pass
            elif token in [IOSGrammarParser.VTP]:
                self.state = 130
                self.vtp_stmt()
                pass
            elif token in [IOSGrammarParser.LOGIN]:
                self.state = 131
                self.login_stmt()
                pass
            elif token in [IOSGrammarParser.IPV6]:
                self.state = 132
                self.ipv6_stmt()
                pass
            elif token in [IOSGrammarParser.MLS]:
                self.state = 133
                self.mls_stmt()
                pass
            elif token in [IOSGrammarParser.KEY]:
                self.state = 134
                self.key_stmt()
                pass
            elif token in [IOSGrammarParser.CRYPTO]:
                self.state = 135
                self.crypto_stmt()
                pass
            elif token in [IOSGrammarParser.ERRDISABLE]:
                self.state = 136
                self.errdisable_stmt()
                pass
            elif token in [IOSGrammarParser.PORT_CHANNEL]:
                self.state = 137
                self.port_channel_stmt()
                pass
            elif token in [IOSGrammarParser.ARCHIVE]:
                self.state = 138
                self.archive_stmt()
                pass
            elif token in [IOSGrammarParser.SPANNING_TREE]:
                self.state = 139
                self.spanning_tree_stmt()
                pass
            elif token in [IOSGrammarParser.VLAN]:
                self.state = 140
                self.vlan_stmt()
                pass
            elif token in [IOSGrammarParser.TRACK]:
                self.state = 141
                self.track_stmt()
                pass
            elif token in [IOSGrammarParser.CLASS_MAP]:
                self.state = 142
                self.class_map_stmt()
                pass
            elif token in [IOSGrammarParser.POLICY_MAP]:
                self.state = 143
                self.policy_map_stmt()
                pass
            elif token in [IOSGrammarParser.INTERFACE]:
                self.state = 144
                self.interface_stmt()
                pass
            elif token in [IOSGrammarParser.ACCESS_LIST]:
                self.state = 145
                self.access_list_stmt()
                pass
            elif token in [IOSGrammarParser.ARP]:
                self.state = 146
                self.arp_stmt()
                pass
            elif token in [IOSGrammarParser.SNMP_SERVER]:
                self.state = 147
                self.snmp_server_stmt()
                pass
            elif token in [IOSGrammarParser.TACACS_SERVER]:
                self.state = 148
                self.tacacs_server_stmt()
                pass
            elif token in [IOSGrammarParser.TACACS]:
                self.state = 149
                self.tacacs_stmt()
                pass
            elif token in [IOSGrammarParser.VSTACK]:
                self.state = 150
                self.vstack_stmt()
                pass
            elif token in [IOSGrammarParser.BANNER]:
                self.state = 151
                self.banner_stmt()
                pass
            elif token in [IOSGrammarParser.LINE]:
                self.state = 152
                self.line_stmt()
                pass
            elif token in [IOSGrammarParser.NTP]:
                self.state = 153
                self.ntp_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Version_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION(self):
            return self.getToken(IOSGrammarParser.VERSION, 0)

        def ID(self):
            return self.getToken(IOSGrammarParser.ID, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_version_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersion_stmt" ):
                listener.enterVersion_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersion_stmt" ):
                listener.exitVersion_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersion_stmt" ):
                return visitor.visitVersion_stmt(self)
            else:
                return visitor.visitChildren(self)




    def version_stmt(self):

        localctx = IOSGrammarParser.Version_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_version_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(IOSGrammarParser.VERSION)
            self.state = 157
            self.match(IOSGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hostname_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HOSTNAME(self):
            return self.getToken(IOSGrammarParser.HOSTNAME, 0)

        def ID(self):
            return self.getToken(IOSGrammarParser.ID, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_hostname_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHostname_stmt" ):
                listener.enterHostname_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHostname_stmt" ):
                listener.exitHostname_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHostname_stmt" ):
                return visitor.visitHostname_stmt(self)
            else:
                return visitor.visitChildren(self)




    def hostname_stmt(self):

        localctx = IOSGrammarParser.Hostname_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hostname_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(IOSGrammarParser.HOSTNAME)
            self.state = 160
            self.match(IOSGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Service_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SERVICE(self):
            return self.getToken(IOSGrammarParser.SERVICE, 0)

        def PAD(self):
            return self.getToken(IOSGrammarParser.PAD, 0)

        def TIMESTAMPS(self):
            return self.getToken(IOSGrammarParser.TIMESTAMPS, 0)

        def PASSWORD_ENCRYPTION(self):
            return self.getToken(IOSGrammarParser.PASSWORD_ENCRYPTION, 0)

        def UNSUPPORTED_TRANSCEIVER(self):
            return self.getToken(IOSGrammarParser.UNSUPPORTED_TRANSCEIVER, 0)

        def UPTIME(self):
            return self.getToken(IOSGrammarParser.UPTIME, 0)

        def DATETIME(self):
            return self.getToken(IOSGrammarParser.DATETIME, 0)

        def LOG_LEVEL(self):
            return self.getToken(IOSGrammarParser.LOG_LEVEL, 0)

        def MSEC(self):
            return self.getToken(IOSGrammarParser.MSEC, 0)

        def LOCALTIME(self):
            return self.getToken(IOSGrammarParser.LOCALTIME, 0)

        def SHOW_TIMEZONE(self):
            return self.getToken(IOSGrammarParser.SHOW_TIMEZONE, 0)

        def YEAR(self):
            return self.getToken(IOSGrammarParser.YEAR, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_service_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterService_stmt" ):
                listener.enterService_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitService_stmt" ):
                listener.exitService_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitService_stmt" ):
                return visitor.visitService_stmt(self)
            else:
                return visitor.visitChildren(self)




    def service_stmt(self):

        localctx = IOSGrammarParser.Service_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_service_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(IOSGrammarParser.SERVICE)
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IOSGrammarParser.PAD]:
                self.state = 163
                self.match(IOSGrammarParser.PAD)
                pass
            elif token in [IOSGrammarParser.TIMESTAMPS]:
                self.state = 164
                self.match(IOSGrammarParser.TIMESTAMPS)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IOSGrammarParser.LOG_LEVEL:
                    self.state = 165
                    self.match(IOSGrammarParser.LOG_LEVEL)


                self.state = 176
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [IOSGrammarParser.UPTIME]:
                    self.state = 168
                    self.match(IOSGrammarParser.UPTIME)
                    pass
                elif token in [IOSGrammarParser.DATETIME]:
                    self.state = 169
                    self.match(IOSGrammarParser.DATETIME)
                    self.state = 171
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==IOSGrammarParser.MSEC:
                        self.state = 170
                        self.match(IOSGrammarParser.MSEC)


                    self.state = 174
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IOSGrammarParser.LOCALTIME) | (1 << IOSGrammarParser.SHOW_TIMEZONE) | (1 << IOSGrammarParser.YEAR))) != 0):
                        self.state = 173
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IOSGrammarParser.LOCALTIME) | (1 << IOSGrammarParser.SHOW_TIMEZONE) | (1 << IOSGrammarParser.YEAR))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()


                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [IOSGrammarParser.PASSWORD_ENCRYPTION]:
                self.state = 178
                self.match(IOSGrammarParser.PASSWORD_ENCRYPTION)
                pass
            elif token in [IOSGrammarParser.UNSUPPORTED_TRANSCEIVER]:
                self.state = 179
                self.match(IOSGrammarParser.UNSUPPORTED_TRANSCEIVER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boot_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOT_START_MARKER(self):
            return self.getToken(IOSGrammarParser.BOOT_START_MARKER, 0)

        def BOOT_END_MARKER(self):
            return self.getToken(IOSGrammarParser.BOOT_END_MARKER, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_boot_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoot_stmt" ):
                listener.enterBoot_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoot_stmt" ):
                listener.exitBoot_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoot_stmt" ):
                return visitor.visitBoot_stmt(self)
            else:
                return visitor.visitChildren(self)




    def boot_stmt(self):

        localctx = IOSGrammarParser.Boot_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_boot_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==IOSGrammarParser.BOOT_START_MARKER or _la==IOSGrammarParser.BOOT_END_MARKER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logging_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGGING(self):
            return self.getToken(IOSGrammarParser.LOGGING, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_logging_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogging_stmt" ):
                listener.enterLogging_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogging_stmt" ):
                listener.exitLogging_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogging_stmt" ):
                return visitor.visitLogging_stmt(self)
            else:
                return visitor.visitChildren(self)




    def logging_stmt(self):

        localctx = IOSGrammarParser.Logging_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logging_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(IOSGrammarParser.LOGGING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enable_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENABLE(self):
            return self.getToken(IOSGrammarParser.ENABLE, 0)

        def CREDENTIAL_TYPE(self):
            return self.getToken(IOSGrammarParser.CREDENTIAL_TYPE, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_enable_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnable_stmt" ):
                listener.enterEnable_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnable_stmt" ):
                listener.exitEnable_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnable_stmt" ):
                return visitor.visitEnable_stmt(self)
            else:
                return visitor.visitChildren(self)




    def enable_stmt(self):

        localctx = IOSGrammarParser.Enable_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_enable_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(IOSGrammarParser.ENABLE)
            self.state = 187
            self.match(IOSGrammarParser.CREDENTIAL_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Username_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USERNAME(self):
            return self.getToken(IOSGrammarParser.USERNAME, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IOSGrammarParser.ID)
            else:
                return self.getToken(IOSGrammarParser.ID, i)

        def CREDENTIAL_TYPE(self):
            return self.getToken(IOSGrammarParser.CREDENTIAL_TYPE, 0)

        def PRIVILEGE(self):
            return self.getToken(IOSGrammarParser.PRIVILEGE, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_username_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsername_stmt" ):
                listener.enterUsername_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsername_stmt" ):
                listener.exitUsername_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsername_stmt" ):
                return visitor.visitUsername_stmt(self)
            else:
                return visitor.visitChildren(self)




    def username_stmt(self):

        localctx = IOSGrammarParser.Username_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_username_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(IOSGrammarParser.USERNAME)
            self.state = 190
            self.match(IOSGrammarParser.ID)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IOSGrammarParser.PRIVILEGE:
                self.state = 191
                self.match(IOSGrammarParser.PRIVILEGE)


            self.state = 194
            self.match(IOSGrammarParser.CREDENTIAL_TYPE)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IOSGrammarParser.ID:
                self.state = 195
                self.match(IOSGrammarParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aaa_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AAA(self):
            return self.getToken(IOSGrammarParser.AAA, 0)

        def NEW_MODEL(self):
            return self.getToken(IOSGrammarParser.NEW_MODEL, 0)

        def aaa_group(self):
            return self.getTypedRuleContext(IOSGrammarParser.Aaa_groupContext,0)


        def aaa_authentication(self):
            return self.getTypedRuleContext(IOSGrammarParser.Aaa_authenticationContext,0)


        def aaa_authorization(self):
            return self.getTypedRuleContext(IOSGrammarParser.Aaa_authorizationContext,0)


        def aaa_accounting(self):
            return self.getTypedRuleContext(IOSGrammarParser.Aaa_accountingContext,0)


        def getRuleIndex(self):
            return IOSGrammarParser.RULE_aaa_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAaa_stmt" ):
                listener.enterAaa_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAaa_stmt" ):
                listener.exitAaa_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAaa_stmt" ):
                return visitor.visitAaa_stmt(self)
            else:
                return visitor.visitChildren(self)




    def aaa_stmt(self):

        localctx = IOSGrammarParser.Aaa_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_aaa_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(IOSGrammarParser.AAA)
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IOSGrammarParser.NEW_MODEL]:
                self.state = 199
                self.match(IOSGrammarParser.NEW_MODEL)
                pass
            elif token in [IOSGrammarParser.GROUP]:
                self.state = 200
                self.aaa_group()
                pass
            elif token in [IOSGrammarParser.AUTHENTICATION]:
                self.state = 201
                self.aaa_authentication()
                pass
            elif token in [IOSGrammarParser.AUTHORIZATION]:
                self.state = 202
                self.aaa_authorization()
                pass
            elif token in [IOSGrammarParser.ACCOUNTING]:
                self.state = 203
                self.aaa_accounting()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aaa_groupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(IOSGrammarParser.GROUP, 0)

        def SERVER(self):
            return self.getToken(IOSGrammarParser.SERVER, 0)

        def ID(self):
            return self.getToken(IOSGrammarParser.ID, 0)

        def suite(self):
            return self.getTypedRuleContext(IOSGrammarParser.SuiteContext,0)


        def getRuleIndex(self):
            return IOSGrammarParser.RULE_aaa_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAaa_group" ):
                listener.enterAaa_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAaa_group" ):
                listener.exitAaa_group(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAaa_group" ):
                return visitor.visitAaa_group(self)
            else:
                return visitor.visitChildren(self)




    def aaa_group(self):

        localctx = IOSGrammarParser.Aaa_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_aaa_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(IOSGrammarParser.GROUP)
            self.state = 207
            self.match(IOSGrammarParser.SERVER)
            self.state = 208
            self.match(IOSGrammarParser.T__0)
            self.state = 209
            self.match(IOSGrammarParser.ID)
            self.state = 210
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aaa_authenticationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTHENTICATION(self):
            return self.getToken(IOSGrammarParser.AUTHENTICATION, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_aaa_authentication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAaa_authentication" ):
                listener.enterAaa_authentication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAaa_authentication" ):
                listener.exitAaa_authentication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAaa_authentication" ):
                return visitor.visitAaa_authentication(self)
            else:
                return visitor.visitChildren(self)




    def aaa_authentication(self):

        localctx = IOSGrammarParser.Aaa_authenticationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_aaa_authentication)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(IOSGrammarParser.AUTHENTICATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aaa_authorizationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTHORIZATION(self):
            return self.getToken(IOSGrammarParser.AUTHORIZATION, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_aaa_authorization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAaa_authorization" ):
                listener.enterAaa_authorization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAaa_authorization" ):
                listener.exitAaa_authorization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAaa_authorization" ):
                return visitor.visitAaa_authorization(self)
            else:
                return visitor.visitChildren(self)




    def aaa_authorization(self):

        localctx = IOSGrammarParser.Aaa_authorizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_aaa_authorization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(IOSGrammarParser.AUTHORIZATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aaa_accountingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCOUNTING(self):
            return self.getToken(IOSGrammarParser.ACCOUNTING, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_aaa_accounting

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAaa_accounting" ):
                listener.enterAaa_accounting(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAaa_accounting" ):
                listener.exitAaa_accounting(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAaa_accounting" ):
                return visitor.visitAaa_accounting(self)
            else:
                return visitor.visitChildren(self)




    def aaa_accounting(self):

        localctx = IOSGrammarParser.Aaa_accountingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_aaa_accounting)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(IOSGrammarParser.ACCOUNTING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TacacsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TACACS(self):
            return self.getToken(IOSGrammarParser.TACACS, 0)

        def server_stmt(self):
            return self.getTypedRuleContext(IOSGrammarParser.Server_stmtContext,0)


        def getRuleIndex(self):
            return IOSGrammarParser.RULE_tacacs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTacacs" ):
                listener.enterTacacs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTacacs" ):
                listener.exitTacacs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTacacs" ):
                return visitor.visitTacacs(self)
            else:
                return visitor.visitChildren(self)




    def tacacs(self):

        localctx = IOSGrammarParser.TacacsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tacacs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(IOSGrammarParser.TACACS)
            self.state = 219
            self.server_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Server_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SERVER(self):
            return self.getToken(IOSGrammarParser.SERVER, 0)

        def ID(self):
            return self.getToken(IOSGrammarParser.ID, 0)

        def NAME(self):
            return self.getToken(IOSGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_server_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServer_stmt" ):
                listener.enterServer_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServer_stmt" ):
                listener.exitServer_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitServer_stmt" ):
                return visitor.visitServer_stmt(self)
            else:
                return visitor.visitChildren(self)




    def server_stmt(self):

        localctx = IOSGrammarParser.Server_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_server_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(IOSGrammarParser.SERVER)
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IOSGrammarParser.ID]:
                self.state = 222
                self.match(IOSGrammarParser.ID)
                pass
            elif token in [IOSGrammarParser.NAME]:
                self.state = 223
                self.match(IOSGrammarParser.NAME)
                self.state = 224
                self.match(IOSGrammarParser.ID)
                pass
            elif token in [IOSGrammarParser.EOF, IOSGrammarParser.NEWLINE]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ip_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IP(self):
            return self.getToken(IOSGrammarParser.IP, 0)

        def TACACS(self):
            return self.getToken(IOSGrammarParser.TACACS, 0)

        def SOURCE_INTERFACE(self):
            return self.getToken(IOSGrammarParser.SOURCE_INTERFACE, 0)

        def ID(self):
            return self.getToken(IOSGrammarParser.ID, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_ip_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIp_stmt" ):
                listener.enterIp_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIp_stmt" ):
                listener.exitIp_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIp_stmt" ):
                return visitor.visitIp_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ip_stmt(self):

        localctx = IOSGrammarParser.Ip_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ip_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(IOSGrammarParser.IP)
            self.state = 228
            self.match(IOSGrammarParser.TACACS)
            self.state = 229
            self.match(IOSGrammarParser.SOURCE_INTERFACE)
            self.state = 230
            self.match(IOSGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Clock_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLOCK(self):
            return self.getToken(IOSGrammarParser.CLOCK, 0)

        def SUMMER_TIME(self):
            return self.getToken(IOSGrammarParser.SUMMER_TIME, 0)

        def ZONE(self):
            return self.getToken(IOSGrammarParser.ZONE, 0)

        def TIMEZONE(self):
            return self.getToken(IOSGrammarParser.TIMEZONE, 0)

        def UPDATE_CALENDAR(self):
            return self.getToken(IOSGrammarParser.UPDATE_CALENDAR, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_clock_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClock_stmt" ):
                listener.enterClock_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClock_stmt" ):
                listener.exitClock_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClock_stmt" ):
                return visitor.visitClock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def clock_stmt(self):

        localctx = IOSGrammarParser.Clock_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_clock_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(IOSGrammarParser.CLOCK)
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IOSGrammarParser.SUMMER_TIME]:
                self.state = 233
                self.match(IOSGrammarParser.SUMMER_TIME)
                self.state = 234
                self.match(IOSGrammarParser.ZONE)
                pass
            elif token in [IOSGrammarParser.TIMEZONE]:
                self.state = 235
                self.match(IOSGrammarParser.TIMEZONE)
                pass
            elif token in [IOSGrammarParser.UPDATE_CALENDAR]:
                self.state = 236
                self.match(IOSGrammarParser.UPDATE_CALENDAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class System_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYSTEM(self):
            return self.getToken(IOSGrammarParser.SYSTEM, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_system_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystem_stmt" ):
                listener.enterSystem_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystem_stmt" ):
                listener.exitSystem_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSystem_stmt" ):
                return visitor.visitSystem_stmt(self)
            else:
                return visitor.visitChildren(self)




    def system_stmt(self):

        localctx = IOSGrammarParser.System_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_system_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(IOSGrammarParser.SYSTEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vtp_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VTP(self):
            return self.getToken(IOSGrammarParser.VTP, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_vtp_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVtp_stmt" ):
                listener.enterVtp_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVtp_stmt" ):
                listener.exitVtp_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVtp_stmt" ):
                return visitor.visitVtp_stmt(self)
            else:
                return visitor.visitChildren(self)




    def vtp_stmt(self):

        localctx = IOSGrammarParser.Vtp_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_vtp_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(IOSGrammarParser.VTP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Login_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGIN(self):
            return self.getToken(IOSGrammarParser.LOGIN, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_login_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogin_stmt" ):
                listener.enterLogin_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogin_stmt" ):
                listener.exitLogin_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogin_stmt" ):
                return visitor.visitLogin_stmt(self)
            else:
                return visitor.visitChildren(self)




    def login_stmt(self):

        localctx = IOSGrammarParser.Login_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_login_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(IOSGrammarParser.LOGIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ipv6_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IPV6(self):
            return self.getToken(IOSGrammarParser.IPV6, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_ipv6_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIpv6_stmt" ):
                listener.enterIpv6_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIpv6_stmt" ):
                listener.exitIpv6_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIpv6_stmt" ):
                return visitor.visitIpv6_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ipv6_stmt(self):

        localctx = IOSGrammarParser.Ipv6_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ipv6_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(IOSGrammarParser.IPV6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mls_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MLS(self):
            return self.getToken(IOSGrammarParser.MLS, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_mls_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMls_stmt" ):
                listener.enterMls_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMls_stmt" ):
                listener.exitMls_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMls_stmt" ):
                return visitor.visitMls_stmt(self)
            else:
                return visitor.visitChildren(self)




    def mls_stmt(self):

        localctx = IOSGrammarParser.Mls_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_mls_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(IOSGrammarParser.MLS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(IOSGrammarParser.KEY, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_key_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey_stmt" ):
                listener.enterKey_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey_stmt" ):
                listener.exitKey_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_stmt" ):
                return visitor.visitKey_stmt(self)
            else:
                return visitor.visitChildren(self)




    def key_stmt(self):

        localctx = IOSGrammarParser.Key_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_key_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(IOSGrammarParser.KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Crypto_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CRYPTO(self):
            return self.getToken(IOSGrammarParser.CRYPTO, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_crypto_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrypto_stmt" ):
                listener.enterCrypto_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrypto_stmt" ):
                listener.exitCrypto_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrypto_stmt" ):
                return visitor.visitCrypto_stmt(self)
            else:
                return visitor.visitChildren(self)




    def crypto_stmt(self):

        localctx = IOSGrammarParser.Crypto_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_crypto_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(IOSGrammarParser.CRYPTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Errdisable_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ERRDISABLE(self):
            return self.getToken(IOSGrammarParser.ERRDISABLE, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_errdisable_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterErrdisable_stmt" ):
                listener.enterErrdisable_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitErrdisable_stmt" ):
                listener.exitErrdisable_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitErrdisable_stmt" ):
                return visitor.visitErrdisable_stmt(self)
            else:
                return visitor.visitChildren(self)




    def errdisable_stmt(self):

        localctx = IOSGrammarParser.Errdisable_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_errdisable_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(IOSGrammarParser.ERRDISABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Port_channel_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PORT_CHANNEL(self):
            return self.getToken(IOSGrammarParser.PORT_CHANNEL, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_port_channel_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPort_channel_stmt" ):
                listener.enterPort_channel_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPort_channel_stmt" ):
                listener.exitPort_channel_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPort_channel_stmt" ):
                return visitor.visitPort_channel_stmt(self)
            else:
                return visitor.visitChildren(self)




    def port_channel_stmt(self):

        localctx = IOSGrammarParser.Port_channel_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_port_channel_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(IOSGrammarParser.PORT_CHANNEL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Archive_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARCHIVE(self):
            return self.getToken(IOSGrammarParser.ARCHIVE, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_archive_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArchive_stmt" ):
                listener.enterArchive_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArchive_stmt" ):
                listener.exitArchive_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArchive_stmt" ):
                return visitor.visitArchive_stmt(self)
            else:
                return visitor.visitChildren(self)




    def archive_stmt(self):

        localctx = IOSGrammarParser.Archive_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_archive_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(IOSGrammarParser.ARCHIVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spanning_tree_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPANNING_TREE(self):
            return self.getToken(IOSGrammarParser.SPANNING_TREE, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_spanning_tree_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpanning_tree_stmt" ):
                listener.enterSpanning_tree_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpanning_tree_stmt" ):
                listener.exitSpanning_tree_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpanning_tree_stmt" ):
                return visitor.visitSpanning_tree_stmt(self)
            else:
                return visitor.visitChildren(self)




    def spanning_tree_stmt(self):

        localctx = IOSGrammarParser.Spanning_tree_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_spanning_tree_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(IOSGrammarParser.SPANNING_TREE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vlan_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VLAN(self):
            return self.getToken(IOSGrammarParser.VLAN, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_vlan_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVlan_stmt" ):
                listener.enterVlan_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVlan_stmt" ):
                listener.exitVlan_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVlan_stmt" ):
                return visitor.visitVlan_stmt(self)
            else:
                return visitor.visitChildren(self)




    def vlan_stmt(self):

        localctx = IOSGrammarParser.Vlan_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_vlan_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(IOSGrammarParser.VLAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Track_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRACK(self):
            return self.getToken(IOSGrammarParser.TRACK, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_track_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrack_stmt" ):
                listener.enterTrack_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrack_stmt" ):
                listener.exitTrack_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrack_stmt" ):
                return visitor.visitTrack_stmt(self)
            else:
                return visitor.visitChildren(self)




    def track_stmt(self):

        localctx = IOSGrammarParser.Track_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_track_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(IOSGrammarParser.TRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_map_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS_MAP(self):
            return self.getToken(IOSGrammarParser.CLASS_MAP, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_class_map_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_map_stmt" ):
                listener.enterClass_map_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_map_stmt" ):
                listener.exitClass_map_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_map_stmt" ):
                return visitor.visitClass_map_stmt(self)
            else:
                return visitor.visitChildren(self)




    def class_map_stmt(self):

        localctx = IOSGrammarParser.Class_map_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_class_map_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(IOSGrammarParser.CLASS_MAP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Policy_map_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POLICY_MAP(self):
            return self.getToken(IOSGrammarParser.POLICY_MAP, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_policy_map_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy_map_stmt" ):
                listener.enterPolicy_map_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy_map_stmt" ):
                listener.exitPolicy_map_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicy_map_stmt" ):
                return visitor.visitPolicy_map_stmt(self)
            else:
                return visitor.visitChildren(self)




    def policy_map_stmt(self):

        localctx = IOSGrammarParser.Policy_map_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_policy_map_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(IOSGrammarParser.POLICY_MAP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(IOSGrammarParser.INTERFACE, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_interface_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_stmt" ):
                listener.enterInterface_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_stmt" ):
                listener.exitInterface_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_stmt" ):
                return visitor.visitInterface_stmt(self)
            else:
                return visitor.visitChildren(self)




    def interface_stmt(self):

        localctx = IOSGrammarParser.Interface_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_interface_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(IOSGrammarParser.INTERFACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_list_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCESS_LIST(self):
            return self.getToken(IOSGrammarParser.ACCESS_LIST, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_access_list_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccess_list_stmt" ):
                listener.enterAccess_list_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccess_list_stmt" ):
                listener.exitAccess_list_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_list_stmt" ):
                return visitor.visitAccess_list_stmt(self)
            else:
                return visitor.visitChildren(self)




    def access_list_stmt(self):

        localctx = IOSGrammarParser.Access_list_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_access_list_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(IOSGrammarParser.ACCESS_LIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arp_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARP(self):
            return self.getToken(IOSGrammarParser.ARP, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_arp_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArp_stmt" ):
                listener.enterArp_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArp_stmt" ):
                listener.exitArp_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArp_stmt" ):
                return visitor.visitArp_stmt(self)
            else:
                return visitor.visitChildren(self)




    def arp_stmt(self):

        localctx = IOSGrammarParser.Arp_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arp_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(IOSGrammarParser.ARP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Snmp_server_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SNMP_SERVER(self):
            return self.getToken(IOSGrammarParser.SNMP_SERVER, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_snmp_server_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSnmp_server_stmt" ):
                listener.enterSnmp_server_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSnmp_server_stmt" ):
                listener.exitSnmp_server_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSnmp_server_stmt" ):
                return visitor.visitSnmp_server_stmt(self)
            else:
                return visitor.visitChildren(self)




    def snmp_server_stmt(self):

        localctx = IOSGrammarParser.Snmp_server_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_snmp_server_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(IOSGrammarParser.SNMP_SERVER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tacacs_server_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TACACS_SERVER(self):
            return self.getToken(IOSGrammarParser.TACACS_SERVER, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_tacacs_server_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTacacs_server_stmt" ):
                listener.enterTacacs_server_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTacacs_server_stmt" ):
                listener.exitTacacs_server_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTacacs_server_stmt" ):
                return visitor.visitTacacs_server_stmt(self)
            else:
                return visitor.visitChildren(self)




    def tacacs_server_stmt(self):

        localctx = IOSGrammarParser.Tacacs_server_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_tacacs_server_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(IOSGrammarParser.TACACS_SERVER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tacacs_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TACACS(self):
            return self.getToken(IOSGrammarParser.TACACS, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_tacacs_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTacacs_stmt" ):
                listener.enterTacacs_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTacacs_stmt" ):
                listener.exitTacacs_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTacacs_stmt" ):
                return visitor.visitTacacs_stmt(self)
            else:
                return visitor.visitChildren(self)




    def tacacs_stmt(self):

        localctx = IOSGrammarParser.Tacacs_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_tacacs_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(IOSGrammarParser.TACACS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vstack_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VSTACK(self):
            return self.getToken(IOSGrammarParser.VSTACK, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_vstack_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVstack_stmt" ):
                listener.enterVstack_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVstack_stmt" ):
                listener.exitVstack_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVstack_stmt" ):
                return visitor.visitVstack_stmt(self)
            else:
                return visitor.visitChildren(self)




    def vstack_stmt(self):

        localctx = IOSGrammarParser.Vstack_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_vstack_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(IOSGrammarParser.VSTACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Banner_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BANNER(self):
            return self.getToken(IOSGrammarParser.BANNER, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_banner_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBanner_stmt" ):
                listener.enterBanner_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBanner_stmt" ):
                listener.exitBanner_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBanner_stmt" ):
                return visitor.visitBanner_stmt(self)
            else:
                return visitor.visitChildren(self)




    def banner_stmt(self):

        localctx = IOSGrammarParser.Banner_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_banner_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(IOSGrammarParser.BANNER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE(self):
            return self.getToken(IOSGrammarParser.LINE, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_line_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_stmt" ):
                listener.enterLine_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_stmt" ):
                listener.exitLine_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_stmt" ):
                return visitor.visitLine_stmt(self)
            else:
                return visitor.visitChildren(self)




    def line_stmt(self):

        localctx = IOSGrammarParser.Line_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_line_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(IOSGrammarParser.LINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ntp_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NTP(self):
            return self.getToken(IOSGrammarParser.NTP, 0)

        def getRuleIndex(self):
            return IOSGrammarParser.RULE_ntp_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNtp_stmt" ):
                listener.enterNtp_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNtp_stmt" ):
                listener.exitNtp_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNtp_stmt" ):
                return visitor.visitNtp_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ntp_stmt(self):

        localctx = IOSGrammarParser.Ntp_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_ntp_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(IOSGrammarParser.NTP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





