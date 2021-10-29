parser grammar IOSParser;

options {
	tokenVocab = IOSLexer;
}

config: (row EOL)+ EOF;
row: (EXCLAMATION | ((NO)? basecommand (subcommand)*));
basecommand: (
		version
		| service
		| hostname
		| BOOT_MARKER
		| LOGGING
		| enable
		| username
	);
subcommand: (ID | WORD);

hostname: HOSTNAME ID;
version: VERSION ID;
service:
	SERVICE (
		PAD
		| TIMESTAMPS (LOG_LEVEL)? DATETIME (DATETIME_UNIT)?
		| PASSWORD_ENCRYPTION
		| UNSUPPORTED_TRANSCEIVER
	);
enable: ENABLE CREDENTIAL_TYPE;
username: USERNAME ID (PRIVILEGE)? CREDENTIAL_TYPE (ID)?;
