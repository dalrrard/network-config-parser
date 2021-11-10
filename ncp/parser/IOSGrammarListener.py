# Generated from /home/user/Projects/network-config-parser/ncp/parser/IOSGrammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IOSGrammarParser import IOSGrammarParser
else:
    from IOSGrammarParser import IOSGrammarParser

# This class defines a complete listener for a parse tree produced by IOSGrammarParser.
class IOSGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by IOSGrammarParser#config.
    def enterConfig(self, ctx:IOSGrammarParser.ConfigContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#config.
    def exitConfig(self, ctx:IOSGrammarParser.ConfigContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#suite.
    def enterSuite(self, ctx:IOSGrammarParser.SuiteContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#suite.
    def exitSuite(self, ctx:IOSGrammarParser.SuiteContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#stmt.
    def enterStmt(self, ctx:IOSGrammarParser.StmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#stmt.
    def exitStmt(self, ctx:IOSGrammarParser.StmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#command.
    def enterCommand(self, ctx:IOSGrammarParser.CommandContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#command.
    def exitCommand(self, ctx:IOSGrammarParser.CommandContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#version_stmt.
    def enterVersion_stmt(self, ctx:IOSGrammarParser.Version_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#version_stmt.
    def exitVersion_stmt(self, ctx:IOSGrammarParser.Version_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#hostname_stmt.
    def enterHostname_stmt(self, ctx:IOSGrammarParser.Hostname_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#hostname_stmt.
    def exitHostname_stmt(self, ctx:IOSGrammarParser.Hostname_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#service_stmt.
    def enterService_stmt(self, ctx:IOSGrammarParser.Service_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#service_stmt.
    def exitService_stmt(self, ctx:IOSGrammarParser.Service_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#boot_stmt.
    def enterBoot_stmt(self, ctx:IOSGrammarParser.Boot_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#boot_stmt.
    def exitBoot_stmt(self, ctx:IOSGrammarParser.Boot_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#logging_stmt.
    def enterLogging_stmt(self, ctx:IOSGrammarParser.Logging_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#logging_stmt.
    def exitLogging_stmt(self, ctx:IOSGrammarParser.Logging_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#enable_stmt.
    def enterEnable_stmt(self, ctx:IOSGrammarParser.Enable_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#enable_stmt.
    def exitEnable_stmt(self, ctx:IOSGrammarParser.Enable_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#username_stmt.
    def enterUsername_stmt(self, ctx:IOSGrammarParser.Username_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#username_stmt.
    def exitUsername_stmt(self, ctx:IOSGrammarParser.Username_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#aaa_stmt.
    def enterAaa_stmt(self, ctx:IOSGrammarParser.Aaa_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#aaa_stmt.
    def exitAaa_stmt(self, ctx:IOSGrammarParser.Aaa_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#aaa_group.
    def enterAaa_group(self, ctx:IOSGrammarParser.Aaa_groupContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#aaa_group.
    def exitAaa_group(self, ctx:IOSGrammarParser.Aaa_groupContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#aaa_authentication.
    def enterAaa_authentication(self, ctx:IOSGrammarParser.Aaa_authenticationContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#aaa_authentication.
    def exitAaa_authentication(self, ctx:IOSGrammarParser.Aaa_authenticationContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#aaa_authorization.
    def enterAaa_authorization(self, ctx:IOSGrammarParser.Aaa_authorizationContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#aaa_authorization.
    def exitAaa_authorization(self, ctx:IOSGrammarParser.Aaa_authorizationContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#aaa_accounting.
    def enterAaa_accounting(self, ctx:IOSGrammarParser.Aaa_accountingContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#aaa_accounting.
    def exitAaa_accounting(self, ctx:IOSGrammarParser.Aaa_accountingContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#tacacs.
    def enterTacacs(self, ctx:IOSGrammarParser.TacacsContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#tacacs.
    def exitTacacs(self, ctx:IOSGrammarParser.TacacsContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#server_stmt.
    def enterServer_stmt(self, ctx:IOSGrammarParser.Server_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#server_stmt.
    def exitServer_stmt(self, ctx:IOSGrammarParser.Server_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#ip_stmt.
    def enterIp_stmt(self, ctx:IOSGrammarParser.Ip_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#ip_stmt.
    def exitIp_stmt(self, ctx:IOSGrammarParser.Ip_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#clock_stmt.
    def enterClock_stmt(self, ctx:IOSGrammarParser.Clock_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#clock_stmt.
    def exitClock_stmt(self, ctx:IOSGrammarParser.Clock_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#system_stmt.
    def enterSystem_stmt(self, ctx:IOSGrammarParser.System_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#system_stmt.
    def exitSystem_stmt(self, ctx:IOSGrammarParser.System_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#vtp_stmt.
    def enterVtp_stmt(self, ctx:IOSGrammarParser.Vtp_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#vtp_stmt.
    def exitVtp_stmt(self, ctx:IOSGrammarParser.Vtp_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#login_stmt.
    def enterLogin_stmt(self, ctx:IOSGrammarParser.Login_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#login_stmt.
    def exitLogin_stmt(self, ctx:IOSGrammarParser.Login_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#ipv6_stmt.
    def enterIpv6_stmt(self, ctx:IOSGrammarParser.Ipv6_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#ipv6_stmt.
    def exitIpv6_stmt(self, ctx:IOSGrammarParser.Ipv6_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#mls_stmt.
    def enterMls_stmt(self, ctx:IOSGrammarParser.Mls_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#mls_stmt.
    def exitMls_stmt(self, ctx:IOSGrammarParser.Mls_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#key_stmt.
    def enterKey_stmt(self, ctx:IOSGrammarParser.Key_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#key_stmt.
    def exitKey_stmt(self, ctx:IOSGrammarParser.Key_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#crypto_stmt.
    def enterCrypto_stmt(self, ctx:IOSGrammarParser.Crypto_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#crypto_stmt.
    def exitCrypto_stmt(self, ctx:IOSGrammarParser.Crypto_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#errdisable_stmt.
    def enterErrdisable_stmt(self, ctx:IOSGrammarParser.Errdisable_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#errdisable_stmt.
    def exitErrdisable_stmt(self, ctx:IOSGrammarParser.Errdisable_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#port_channel_stmt.
    def enterPort_channel_stmt(self, ctx:IOSGrammarParser.Port_channel_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#port_channel_stmt.
    def exitPort_channel_stmt(self, ctx:IOSGrammarParser.Port_channel_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#archive_stmt.
    def enterArchive_stmt(self, ctx:IOSGrammarParser.Archive_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#archive_stmt.
    def exitArchive_stmt(self, ctx:IOSGrammarParser.Archive_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#spanning_tree_stmt.
    def enterSpanning_tree_stmt(self, ctx:IOSGrammarParser.Spanning_tree_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#spanning_tree_stmt.
    def exitSpanning_tree_stmt(self, ctx:IOSGrammarParser.Spanning_tree_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#vlan_stmt.
    def enterVlan_stmt(self, ctx:IOSGrammarParser.Vlan_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#vlan_stmt.
    def exitVlan_stmt(self, ctx:IOSGrammarParser.Vlan_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#track_stmt.
    def enterTrack_stmt(self, ctx:IOSGrammarParser.Track_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#track_stmt.
    def exitTrack_stmt(self, ctx:IOSGrammarParser.Track_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#class_map_stmt.
    def enterClass_map_stmt(self, ctx:IOSGrammarParser.Class_map_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#class_map_stmt.
    def exitClass_map_stmt(self, ctx:IOSGrammarParser.Class_map_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#policy_map_stmt.
    def enterPolicy_map_stmt(self, ctx:IOSGrammarParser.Policy_map_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#policy_map_stmt.
    def exitPolicy_map_stmt(self, ctx:IOSGrammarParser.Policy_map_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#interface_stmt.
    def enterInterface_stmt(self, ctx:IOSGrammarParser.Interface_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#interface_stmt.
    def exitInterface_stmt(self, ctx:IOSGrammarParser.Interface_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#access_list_stmt.
    def enterAccess_list_stmt(self, ctx:IOSGrammarParser.Access_list_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#access_list_stmt.
    def exitAccess_list_stmt(self, ctx:IOSGrammarParser.Access_list_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#arp_stmt.
    def enterArp_stmt(self, ctx:IOSGrammarParser.Arp_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#arp_stmt.
    def exitArp_stmt(self, ctx:IOSGrammarParser.Arp_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#snmp_server_stmt.
    def enterSnmp_server_stmt(self, ctx:IOSGrammarParser.Snmp_server_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#snmp_server_stmt.
    def exitSnmp_server_stmt(self, ctx:IOSGrammarParser.Snmp_server_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#tacacs_server_stmt.
    def enterTacacs_server_stmt(self, ctx:IOSGrammarParser.Tacacs_server_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#tacacs_server_stmt.
    def exitTacacs_server_stmt(self, ctx:IOSGrammarParser.Tacacs_server_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#tacacs_stmt.
    def enterTacacs_stmt(self, ctx:IOSGrammarParser.Tacacs_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#tacacs_stmt.
    def exitTacacs_stmt(self, ctx:IOSGrammarParser.Tacacs_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#vstack_stmt.
    def enterVstack_stmt(self, ctx:IOSGrammarParser.Vstack_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#vstack_stmt.
    def exitVstack_stmt(self, ctx:IOSGrammarParser.Vstack_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#banner_stmt.
    def enterBanner_stmt(self, ctx:IOSGrammarParser.Banner_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#banner_stmt.
    def exitBanner_stmt(self, ctx:IOSGrammarParser.Banner_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#line_stmt.
    def enterLine_stmt(self, ctx:IOSGrammarParser.Line_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#line_stmt.
    def exitLine_stmt(self, ctx:IOSGrammarParser.Line_stmtContext):
        pass


    # Enter a parse tree produced by IOSGrammarParser#ntp_stmt.
    def enterNtp_stmt(self, ctx:IOSGrammarParser.Ntp_stmtContext):
        pass

    # Exit a parse tree produced by IOSGrammarParser#ntp_stmt.
    def exitNtp_stmt(self, ctx:IOSGrammarParser.Ntp_stmtContext):
        pass



del IOSGrammarParser