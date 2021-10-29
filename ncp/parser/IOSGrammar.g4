grammar IOSGrammar;

tokens {
	INDENT,
	DEDENT
}

config: (NEWLINE | stmt)* EOF;

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
		| logging
		| enable
		| username
		| aaa
		| server
		| ip
	);

version_stmt: VERSION ID;
hostname_stmt: HOSTNAME ID;
service_stmt: SERVICE;
boot_stmt: BOOT_START_MARKER | BOOT_END_MARKER;
logging: LOGGING;
enable: ENABLE;
username: USERNAME;
aaa:
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

tacacs: TACACS server;
server: SERVER (ID | (NAME ID))?;
ip: IP TACACS SOURCE_INTERFACE ID;

EXCLAMATION: '!';
NO: 'no';
SERVICE: 'service';
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
LOG: 'log';
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

NEWLINE: ( '\r'? '\n' | '\r' | '\f') SPACES?;

ID: (WORD | IPV4 | INT+ | '.' | [+_:/=,$#^()\-])+;

WORD: [a-zA-Z\-]+;

IPV4: OCTET '.' OCTET '.' OCTET '.' OCTET;

fragment OCTET: (INT (INT (INT)?)?);

INT: [0-9];

fragment SPACES: [ \t]+;
