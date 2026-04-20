from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch %s connected", event.dpid)

def _handle_PortStatus(event):
    port = event.ofp.desc.port_no
    reason = event.ofp.reason

    if reason == of.OFPPR_DELETE:
        log.info("LINK DOWN detected on port %s", port)
    elif reason == of.OFPPR_ADD:
        log.info("LINK UP detected on port %s", port)
    elif reason == of.OFPPR_MODIFY:
        if event.ofp.desc.config & of.OFPPC_PORT_DOWN:
            log.info("PORT DOWN (Link Failure) on port %s", port)
        else:
            log.info("PORT UP on port %s", port)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PortStatus", _handle_PortStatus)
    log.info("Link Failure Detection Module Loaded")
def _handle_PortStatus(event):
    dpid = event.dpid
    port = event.ofp.desc.port_no
    reason = event.ofp.reason

    if reason == of.OFPPR_DELETE:
        log.info("SWITCH %s: LINK REMOVED on port %s", dpid, port)

    elif reason == of.OFPPR_ADD:
        log.info("SWITCH %s: LINK ADDED on port %s", dpid, port)

    elif reason == of.OFPPR_MODIFY:
        if event.ofp.desc.config & of.OFPPC_PORT_DOWN:
            log.info("🚨 LINK FAILURE: Switch %s Port %s DOWN", dpid, port)
        else:
            log.info("✅ LINK RECOVERY: Switch %s Port %s UP", dpid, port)
