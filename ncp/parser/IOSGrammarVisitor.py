# Generated from /home/user/Projects/network-config-parser/ncp/parser/IOSGrammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IOSGrammarParser import IOSGrammarParser
else:
    from IOSGrammarParser import IOSGrammarParser

# This class defines a complete generic visitor for a parse tree produced by IOSGrammarParser.

class IOSGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IOSGrammarParser#config.
    def visitConfig(self, ctx:IOSGrammarParser.ConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#suite.
    def visitSuite(self, ctx:IOSGrammarParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#stmt.
    def visitStmt(self, ctx:IOSGrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#command.
    def visitCommand(self, ctx:IOSGrammarParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#version_stmt.
    def visitVersion_stmt(self, ctx:IOSGrammarParser.Version_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#hostname_stmt.
    def visitHostname_stmt(self, ctx:IOSGrammarParser.Hostname_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#service_stmt.
    def visitService_stmt(self, ctx:IOSGrammarParser.Service_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#boot_stmt.
    def visitBoot_stmt(self, ctx:IOSGrammarParser.Boot_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#logging_stmt.
    def visitLogging_stmt(self, ctx:IOSGrammarParser.Logging_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#enable_stmt.
    def visitEnable_stmt(self, ctx:IOSGrammarParser.Enable_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#username_stmt.
    def visitUsername_stmt(self, ctx:IOSGrammarParser.Username_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#aaa_stmt.
    def visitAaa_stmt(self, ctx:IOSGrammarParser.Aaa_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#aaa_group.
    def visitAaa_group(self, ctx:IOSGrammarParser.Aaa_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#aaa_authentication.
    def visitAaa_authentication(self, ctx:IOSGrammarParser.Aaa_authenticationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#aaa_authorization.
    def visitAaa_authorization(self, ctx:IOSGrammarParser.Aaa_authorizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#aaa_accounting.
    def visitAaa_accounting(self, ctx:IOSGrammarParser.Aaa_accountingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#tacacs.
    def visitTacacs(self, ctx:IOSGrammarParser.TacacsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#server_stmt.
    def visitServer_stmt(self, ctx:IOSGrammarParser.Server_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#ip_stmt.
    def visitIp_stmt(self, ctx:IOSGrammarParser.Ip_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#clock_stmt.
    def visitClock_stmt(self, ctx:IOSGrammarParser.Clock_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#system_stmt.
    def visitSystem_stmt(self, ctx:IOSGrammarParser.System_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#vtp_stmt.
    def visitVtp_stmt(self, ctx:IOSGrammarParser.Vtp_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#login_stmt.
    def visitLogin_stmt(self, ctx:IOSGrammarParser.Login_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#ipv6_stmt.
    def visitIpv6_stmt(self, ctx:IOSGrammarParser.Ipv6_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#mls_stmt.
    def visitMls_stmt(self, ctx:IOSGrammarParser.Mls_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#key_stmt.
    def visitKey_stmt(self, ctx:IOSGrammarParser.Key_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#crypto_stmt.
    def visitCrypto_stmt(self, ctx:IOSGrammarParser.Crypto_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#errdisable_stmt.
    def visitErrdisable_stmt(self, ctx:IOSGrammarParser.Errdisable_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#port_channel_stmt.
    def visitPort_channel_stmt(self, ctx:IOSGrammarParser.Port_channel_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#archive_stmt.
    def visitArchive_stmt(self, ctx:IOSGrammarParser.Archive_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#spanning_tree_stmt.
    def visitSpanning_tree_stmt(self, ctx:IOSGrammarParser.Spanning_tree_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#vlan_stmt.
    def visitVlan_stmt(self, ctx:IOSGrammarParser.Vlan_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#track_stmt.
    def visitTrack_stmt(self, ctx:IOSGrammarParser.Track_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#class_map_stmt.
    def visitClass_map_stmt(self, ctx:IOSGrammarParser.Class_map_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#policy_map_stmt.
    def visitPolicy_map_stmt(self, ctx:IOSGrammarParser.Policy_map_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#interface_stmt.
    def visitInterface_stmt(self, ctx:IOSGrammarParser.Interface_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#access_list_stmt.
    def visitAccess_list_stmt(self, ctx:IOSGrammarParser.Access_list_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#arp_stmt.
    def visitArp_stmt(self, ctx:IOSGrammarParser.Arp_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#snmp_server_stmt.
    def visitSnmp_server_stmt(self, ctx:IOSGrammarParser.Snmp_server_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#tacacs_server_stmt.
    def visitTacacs_server_stmt(self, ctx:IOSGrammarParser.Tacacs_server_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#tacacs_stmt.
    def visitTacacs_stmt(self, ctx:IOSGrammarParser.Tacacs_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#vstack_stmt.
    def visitVstack_stmt(self, ctx:IOSGrammarParser.Vstack_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#banner_stmt.
    def visitBanner_stmt(self, ctx:IOSGrammarParser.Banner_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#line_stmt.
    def visitLine_stmt(self, ctx:IOSGrammarParser.Line_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOSGrammarParser#ntp_stmt.
    def visitNtp_stmt(self, ctx:IOSGrammarParser.Ntp_stmtContext):
        return self.visitChildren(ctx)



del IOSGrammarParser