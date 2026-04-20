# SDN-based Link Failure Detection using POX and Mininet

## 📌 Problem Statement

This project demonstrates how link failures are detected in a Software Defined Network (SDN) using Mininet and a POX controller. The controller monitors network events and identifies when a link between switches goes down.

---

## 🎯 Objectives

* Detect link failures in an SDN environment
* Observe the impact of failures on network connectivity
* Log failure and recovery events using the controller
* Validate behavior using network testing tools

---

## 🛠️ Technologies Used

* **Mininet** – Network emulation
* **POX Controller** – SDN controller
* **OpenFlow 1.0** – Communication protocol
* **OVS (Open vSwitch)** – Software switch

---

## 🏗️ Network Topology

A simple linear topology is used:

```
h1 ---- s1 ---- s2 ---- h2
```

* h1, h2 → Hosts
* s1, s2 → Switches

---

## ⚙️ Setup Instructions

### 1. Start POX Controller

```bash
cd ~/pox
./pox.py log.level --DEBUG openflow.of_01 misc.link_failure forwarding.hub
```

---

### 2. Start Mininet

```bash
sudo mn --topo linear,2 --controller=remote,ip=127.0.0.1,port=6633
```

---

## 🧪 Test Scenarios

### ✅ Normal Scenario

```bash
pingall
```

**Result:** 0% packet loss (successful communication)

---

### ❌ Link Failure Scenario

```bash
link s1 s2 down
pingall
```

**Result:** 100% packet loss (communication failure)

---

### 🔄 Link Recovery Scenario

```bash
link s1 s2 up
pingall
```

**Result:** Network connectivity restored

---

## 🔍 Detection Mechanism

* The controller listens for **OpenFlow PortStatus events**
* When a link fails, the corresponding ports go down
* The controller logs:

  * Link failure (port down)
  * Link recovery (port up)

Example log:

```
LINK FAILURE: Switch 1 Port 2 DOWN
LINK RECOVERY: Switch 1 Port 2 UP
```

---

## 📊 Observations

* Network connectivity is lost when the link fails
* Packet loss increases to 100%
* Throughput drops to zero (using iperf)
* Controller successfully detects and logs events

---

## 📷 Proof of Execution

Screenshots included in the `screenshots/` folder:

* Normal operation (ping success)
* Link failure (ping failure)
* Controller logs
* (Optional) iperf results

---

## 📚 Conclusion

This project successfully demonstrates how SDN enables centralized monitoring and detection of network failures. The controller detects link failures in real time and reflects their impact on network behavior.

---

## 🎤 Viva Summary (Short Explanation)

This project uses a POX controller to detect link failures in an SDN environment. When a link goes down, switches send PortStatus messages to the controller. The controller logs the failure, and network communication is disrupted, which is verified using ping and iperf.

---

