# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

HOST_METRICS = {
    'sys.resourceMemConsumed.latest',
    'mem.sharedcommon.avg',
    'sys.resourceCpuRun5.latest',
    'sys.resourceMemSwapped.latest',
    'datastore.datastoreReadOIO.latest',
    'sys.resourceCpuAllocShares.latest',
    'sys.resourceCpuUsage.avg',
    'cpu.usagemhz.avg',
    'cpu.wait.sum',
    'mem.vmmemctl.avg',
    'datastore.datastoreReadBytes.latest',
    'disk.busResets.sum',
    'datastore.datastoreVMObservedLatency.latest',
    'disk.totalReadLatency.avg',
    'hbr.hbrNetRx.avg',
    'net.packetsTx.sum',
    'mem.llSwapUsed.avg',
    'sys.resourceCpuMaxLimited1.latest',
    'disk.numberRead.sum',
    'net.received.avg',
    'disk.commandsAborted.sum',
    'rescpu.runpk1.latest',
    'cpu.swapwait.sum',
    'mem.swapin.avg',
    'cpu.used.sum',
    'mem.vmfs.pbc.sizeMax.latest',
    'datastore.datastoreNormalWriteLatency.latest',
    'datastore.datastoreWriteIops.latest',
    'mem.unreserved.avg',
    'mem.shared.avg',
    'storagePath.write.avg',
    'cpu.demand.avg',
    'mem.reservedCapacity.avg',
    'rescpu.samplePeriod.latest',
    'storagePath.totalWriteLatency.avg',
    'power.power.avg',
    'disk.commands.sum',
    'rescpu.actpk15.latest',
    'datastore.write.avg',
    'storagePath.numberWriteAveraged.avg',
    'datastore.datastoreMaxQueueDepth.latest',
    'sys.resourceMemZero.latest',
    'mem.overhead.avg',
    'storagePath.commandsAveraged.avg',
    'datastore.read.avg',
    'disk.numberWriteAveraged.avg',
    'mem.vmfs.pbc.capMissRatio.latest',
    'datastore.totalWriteLatency.avg',
    'mem.llSwapInRate.avg',
    'rescpu.sampleCount.latest',
    'mem.llSwapIn.avg',
    'mem.heapfree.avg',
    'mem.compressionRate.avg',
    'storagePath.read.avg',
    'storagePath.maxTotalLatency.latest',
    'storageAdapter.numberWriteAveraged.avg',
    'disk.totalWriteLatency.avg',
    'net.multicastTx.sum',
    'net.broadcastTx.sum',
    'cpu.usage.avg',
    'net.packetsRx.sum',
    'mem.decompressionRate.avg',
    'mem.granted.avg',
    'net.broadcastRx.sum',
    'storagePath.numberReadAveraged.avg',
    'disk.write.avg',
    'storageAdapter.totalWriteLatency.avg',
    'disk.maxQueueDepth.avg',
    'datastore.unmapSize.sum',
    'sys.resourceCpuAct5.latest',
    'sys.resourceMemAllocMax.latest',
    'cpu.costop.sum',
    'net.usage.avg',
    'mem.swapoutRate.avg',
    'mem.state.latest',
    'mem.llSwapOut.avg',
    'datastore.datastoreWriteBytes.latest',
    'storagePath.totalReadLatency.avg',
    'net.droppedRx.sum',
    'mem.swapinRate.avg',
    'rescpu.runpk5.latest',
    'rescpu.runav5.latest',
    'storageAdapter.write.avg',
    'sys.resourceFdUsage.latest',
    'cpu.totalCapacity.avg',
    'datastore.sizeNormalizedDatastoreLatency.avg',
    'net.unknownProtos.sum',
    'disk.queueLatency.avg',
    'storageAdapter.commandsAveraged.avg',
    'net.bytesTx.avg',
    'datastore.totalReadLatency.avg',
    'rescpu.actpk5.latest',
    'datastore.datastoreReadLoadMetric.latest',
    'disk.numberWrite.sum',
    'storageAdapter.maxTotalLatency.latest',
    'cpu.reservedCapacity.avg',
    'cpu.utilization.avg',
    'disk.deviceLatency.avg',
    'mem.llSwapOutRate.avg',
    'disk.usage.avg',
    'sys.resourceMemShared.latest',
    'disk.deviceReadLatency.avg',
    'disk.maxTotalLatency.latest',
    'hbr.hbrNumVms.avg',
    'disk.queueReadLatency.avg',
    'disk.totalLatency.avg',
    'sys.resourceCpuRun1.latest',
    'datastore.datastoreWriteOIO.latest',
    'datastore.numberWriteAveraged.avg',
    'sys.resourceMemCow.latest',
    'cpu.latency.avg',
    'cpu.idle.sum',
    'rescpu.runpk15.latest',
    'mem.vmfs.pbc.size.latest',
    'hbr.hbrNetTx.avg',
    'storageAdapter.totalReadLatency.avg',
    'power.powerCap.avg',
    'rescpu.runav1.latest',
    'datastore.maxTotalLatency.latest',
    'rescpu.runav15.latest',
    'sys.resourceMemAllocShares.latest',
    'storageAdapter.read.avg',
    'net.droppedTx.sum',
    'datastore.datastoreReadIops.latest',
    'net.errorsTx.sum',
    'mem.heap.avg',
    'mem.swapused.avg',
    'mem.sysUsage.avg',
    'cpu.ready.sum',
    'rescpu.maxLimited1.latest',
    'mem.zero.avg',
    'datastore.datastoreIops.avg',
    'sys.resourceMemMapped.latest',
    'rescpu.actav1.latest',
    'rescpu.actpk1.latest',
    'datastore.siocActiveTimePercentage.avg',
    'datastore.unmapIOs.sum',
    'sys.resourceMemAllocMin.latest',
    'mem.lowfreethreshold.avg',
    'mem.latency.avg',
    'datastore.datastoreNormalReadLatency.latest',
    'mem.totalCapacity.avg',
    'sys.resourceMemOverhead.latest',
    'disk.kernelWriteLatency.avg',
    'mem.activewrite.avg',
    'net.multicastRx.sum',
    'datastore.datastoreWriteLoadMetric.latest',
    'sys.resourceMemTouched.latest',
    'sys.resourceCpuAllocMin.latest',
    'rescpu.actav15.latest',
    'mem.vmfs.pbc.workingSet.latest',
    'disk.numberReadAveraged.avg',
    'disk.read.avg',
    'storageAdapter.numberReadAveraged.avg',
    'power.energy.sum',
    'mem.vmfs.pbc.overhead.latest',
    'mem.active.avg',
    'disk.kernelLatency.avg',
    'net.transmitted.avg',
    'mem.usage.avg',
    'sys.resourceCpuMaxLimited5.latest',
    'mem.vmfs.pbc.workingSetMax.latest',
    'disk.commandsAveraged.avg',
    'sys.uptime.latest',
    'net.errorsRx.sum',
    'disk.queueWriteLatency.avg',
    'datastore.numberReadAveraged.avg',
    'rescpu.actav5.latest',
    'net.bytesRx.avg',
    'mem.compressed.avg',
    'disk.deviceWriteLatency.avg',
    'rescpu.maxLimited5.latest',
    'cpu.readiness.avg',
    'sys.resourceCpuAct1.latest',
    'disk.kernelReadLatency.avg',
    'cpu.coreUtilization.avg',
    'mem.swapout.avg',
    'mem.consumed.avg',
    'rescpu.maxLimited15.latest',
}
