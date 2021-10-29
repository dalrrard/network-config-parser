lexer grammar IOSLexer;

channels {
	WHITESPACE
}

EXCLAMATION: '!';

NO: 'no';

VERSION: 'version';

LOG_LEVEL: 'debug' | 'log' | 'info';

DATETIME: 'datetime';

DATETIME_UNIT: 'msec';

SERVICE: 'service';

PAD: 'pad';

TIMESTAMPS: 'timestamps';

PASSWORD_ENCRYPTION: 'password-encryption';

UNSUPPORTED_TRANSCEIVER: 'unsupported-transceiver';

HOSTNAME: 'hostname';

BOOT_MARKER: 'boot-start-marker' | 'boot-end-marker';

LOGGING: 'logging';

ENABLE: 'enable';

CREDENTIAL_TYPE: ('password' | 'secret') (WS INT)?;

USERNAME: 'username';

PRIVILEGE: 'privilege' WS (INT (INT)?);

AAA: 'aaa';

CLOCK: 'clock';

SYSTEM: 'system';

VTP: 'vtp';

IP: 'ip';

LOGIN: 'login';

IPV6: 'ipv6';

MLS: 'mls';

KEY: 'key';

ERRDISABLE: 'errdisable';

PORT_CHANNEL: 'port-channel';

ARCHIVE: 'archive';

SPANNING_TREE: 'spanning-tree';

VLAN: 'vlan';

CLASS_MAP: 'class-map';

POLICY_MAP: 'policy-map';

VPDN: 'vpdn';

INTERFACE: 'interface';

BRIDGE: 'bridge';

CRYPTO: 'crypto';

RADIUS_SERVER: 'radius-server';

ROUTER: 'router';

ARP: 'arp';

SNMP_SERVER: 'snmp-server';

TACACS_SERVER: 'tacacs-server';

VSTACK: 'vstack';

BANNER: 'banner';

ID: (WORD | IPV4 | INT+ | '.' | [+_:/=,$#^()\-])+;

WORD: [a-zA-Z\-]+;

IPV4: OCTET '.' OCTET '.' OCTET '.' OCTET;

fragment OCTET: (INT (INT (INT)?)?);

INT: [0-9];

WS: [ \t] -> channel(WHITESPACE);

IGNORE: (
		'Building configuration...'
		| 'Current configuration : ' INT+ WS 'bytes'
	) -> skip;
EOL: '\r'? '\n';
