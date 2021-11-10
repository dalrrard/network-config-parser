grammar IOSGrammar;

tokens {
	INDENT,
	DEDENT
}

config: (NEWLINE | stmt)* END EOF;

IGNORE: (
		'Building configuration...'
		| 'Current configuration : ' INT+ SPACES 'bytes'
		| SPACES
	) -> skip;

suite: NEWLINE INDENT stmt+ DEDENT;

stmt: (EXCLAMATION | ((NO)? command)) NEWLINE;

command: (
		version_stmt
		| hostname_stmt
		| service_stmt
		| boot_stmt
		| logging_stmt
		| enable_stmt
		| username_stmt
		| aaa_stmt
		| server_stmt
		| ip_stmt
		| clock_stmt
		| system_stmt
		| vtp_stmt
		| login_stmt
		| ipv6_stmt
		| mls_stmt
		| key_stmt
		| crypto_stmt
		| errdisable_stmt
		| port_channel_stmt
		| archive_stmt
		| spanning_tree_stmt
		| vlan_stmt
		| track_stmt
		| class_map_stmt
		| policy_map_stmt
		| interface_stmt
		| access_list_stmt
		| arp_stmt
		| snmp_server_stmt
		| tacacs_server_stmt
		| tacacs_stmt
		| vstack_stmt
		| banner_stmt
		| line_stmt
		| ntp_stmt
	);

version_stmt: VERSION ID;
hostname_stmt: HOSTNAME ID;
// service_stmt: SERVICE;
service_stmt:
	SERVICE (
		PAD
		| TIMESTAMPS (LOG_LEVEL)? (
			UPTIME
			| DATETIME (MSEC)? (LOCALTIME | SHOW_TIMEZONE | YEAR)?
		)
		| PASSWORD_ENCRYPTION
		| UNSUPPORTED_TRANSCEIVER
	);
boot_stmt: BOOT_START_MARKER | BOOT_END_MARKER;
logging_stmt: LOGGING;
// enable: ENABLE;
enable_stmt: ENABLE CREDENTIAL_TYPE;
// username_stmt: USERNAME;
username_stmt: USERNAME ID (PRIVILEGE)? CREDENTIAL_TYPE (ID)?;
aaa_stmt:
	AAA (
		NEW_MODEL
		| aaa_group
		| aaa_authentication
		| aaa_authorization
		| aaa_accounting
	);

aaa_group: GROUP SERVER 'tacacs+' ID suite;
aaa_authentication: AUTHENTICATION;
aaa_authorization: AUTHORIZATION;
aaa_accounting: ACCOUNTING;

tacacs: TACACS server_stmt;
server_stmt: SERVER (ID | (NAME ID))?;
ip_stmt: IP TACACS SOURCE_INTERFACE ID;

clock_stmt:
	CLOCK (SUMMER_TIME ZONE | TIMEZONE | UPDATE_CALENDAR);
system_stmt: SYSTEM;
vtp_stmt: VTP;
login_stmt: LOGIN;
ipv6_stmt: IPV6;
mls_stmt: MLS;
key_stmt: KEY;
crypto_stmt: CRYPTO;
errdisable_stmt: ERRDISABLE;
port_channel_stmt: PORT_CHANNEL;
archive_stmt: ARCHIVE;
spanning_tree_stmt: SPANNING_TREE;
vlan_stmt: VLAN;
track_stmt: TRACK;
class_map_stmt: CLASS_MAP;
policy_map_stmt: POLICY_MAP;
interface_stmt: INTERFACE;
access_list_stmt: ACCESS_LIST;
arp_stmt: ARP;
snmp_server_stmt: SNMP_SERVER;
tacacs_server_stmt: TACACS_SERVER;
tacacs_stmt: TACACS;
vstack_stmt: VSTACK;
banner_stmt: BANNER;
line_stmt: LINE;
ntp_stmt: NTP;

EXCLAMATION: '!';
NO: 'no';
SERVICE: 'service';
PAD: 'pad';
TIMESTAMPS: 'timestamps';
LOG_LEVEL: 'debug' | 'log' | 'info';
UPTIME: 'uptime';
DATETIME: 'datetime';
MSEC: 'msec';
LOCALTIME: 'localtime';
SHOW_TIMEZONE: 'show-timezone';
YEAR: 'year';
PASSWORD_ENCRYPTION: 'password-encryption';
UNSUPPORTED_TRANSCEIVER: 'unsupported-transceiver';
BANNER: 'banner';
PRIORITY_QUEUE: 'priority-queue';
BOOT_START_MARKER: 'boot-start-marker';
PATH: 'path';
NTP: 'ntp';
SUBJECT_NAME: 'subject-name';
FQDN: 'fqdn';
VLAN: 'vlan';
AF_INTERFACE: 'af-interface';
SNMP_SERVER: 'snmp-server';
PERMIT: 'permit';
PORT_CHANNEL: 'port-channel';
ACCESS_LIST: 'access-list';
HOSTNAME: 'hostname';
MTU: 'mtu';
REVOCATION_CHECK: 'revocation-check';
TIME_PERIOD: 'time-period';
ICMP_ECHO: 'icmp-echo';
SERVICE_FAMILY: 'service-family';
END: 'end';
ARP: 'arp';
STORM_CONTROL: 'storm-control';
VERSION: 'version';
MLS: 'mls';
NAME: 'name';
AUTO: 'auto';
CLASS_MAP: 'class-map';
PRIVATE_VLAN: 'private-vlan';
CHANNEL_PROTOCOL: 'channel-protocol';
ADDRESS_FAMILY: 'address-family';
FREQUENCY: 'frequency';
SWITCHPORT: 'switchport';
MATCH: 'match';
ROLLBACK: 'rollback';
HIDEKEYS: 'hidekeys';
CLOCK: 'clock';
READ_CALENDAR: 'read-calendar';
SUMMER_TIME: 'summer-time';
ZONE:
	'GMT'
	| 'BST'
	| 'IST'
	| 'WET'
	| 'WEST'
	| 'CET'
	| 'CEST'
	| 'EET'
	| 'EEST'
	| 'MSK'
	| 'MSD'
	| 'AST'
	| 'ADT'
	| 'ET'
	| 'EST'
	| 'EDT'
	| 'CT'
	| 'CST'
	| 'CDT'
	| 'MT'
	| 'MST'
	| 'MDT'
	| 'PT'
	| 'PST'
	| 'PDT'
	| 'AKST'
	| 'AKDT'
	| 'HST'
	| 'WST';
TIMEZONE: 'timezone';
UPDATE_CALENDAR: 'update-calendar';
CRYPTO: 'crypto';
ACTION: 'action';
IPV6: 'ipv6';
TACACS_SERVER: 'tacacs-server';
EXIT_ADDRESS_FAMILY: 'exit-address-family';
SRR_QUEUE: 'srr-queue';
STATE: 'state';
TRACK: 'track';
TOPOLOGY: 'topology';
POLICE: 'police';
ENROLLMENT: 'enrollment';
ADDRESS: 'address';
SERVER: 'server';
SET: 'set';
EIGRP: 'eigrp';
TIMEOUT: 'timeout';
DESCRIPTION: 'description';
WRITE_MEMORY: 'write-memory';
ROUTER: 'router';
AAA: 'aaa';
GROUP: 'group';
NEW_MODEL: 'new-model';
AUTHENTICATION: 'authentication';
AUTHORIZATION: 'authorization';
ACCOUNTING: 'accounting';
SOURCE_INTERFACE: 'source-interface';
VTP: 'vtp';
LENGTH: 'length';
CHANNEL_GROUP: 'channel-group';
KEY_STRING: 'key-string';
KEY: 'key';
CERTIFICATE: 'certificate';
USERNAME: 'username';
PRIVILEGE: 'privilege' (INT (INT)?);
EXIT_AF_INTERFACE: 'exit-af-interface';
DENY: 'deny';
SPANNING_TREE: 'spanning-tree';
SHUTDOWN: 'shutdown';
LOGIN: 'login';
EXIT_AF_TOPOLOGY: 'exit-af-topology';
SERVICE_POLICY: 'service-policy';
QUIT: 'quit';
ARCHIVE: 'archive';
EXIT_SERVICE_FAMILY: 'exit-service-family';
NOTIFY: 'notify';
NETWORK: 'network';
RECORD: 'record';
ENABLE: 'enable';
CREDENTIAL_TYPE: ('password' | 'secret') (INT)?;
IP: 'ip';
SYSTEM: 'system';
QUEUE_SET: 'queue-set';
INTERFACE: 'interface';
BOOT_END_MARKER: 'boot-end-marker';
POLICY_MAP: 'policy-map';
LOGGING: 'logging';
LINE: 'line';
PASSIVE_INTERFACE: 'passive-interface';
EXEC_TIMEOUT: 'exec-timeout';
TACACS: 'tacacs';
EXIT_SF_TOPOLOGY: 'exit-sf-topology';
CLASS: 'class';
ERRDISABLE: 'errdisable';
VPDN: 'vpdn';
BRIDGE: 'bridge';
RADIUS_SERVER: 'radius-server';
VSTACK: 'vstack';

NEWLINE: ( '\r'? '\n' | '\r' | '\f') SPACES?;

ID: (WORD | IPV4 | INT+ | '.' | [+_:/=,$#^()\-])+;

WORD: [a-zA-Z\-]+;

IPV4: OCTET '.' OCTET '.' OCTET '.' OCTET;

fragment OCTET: (INT (INT (INT)?)?);

INT: [0-9];

fragment SPACES: [ \t]+;
