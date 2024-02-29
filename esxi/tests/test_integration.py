# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import logging

import pytest

from datadog_checks.esxi import EsxiCheck

from .common import ALL_VCSIM_HOST_METRICS_WITH_VALS, FLAKEY_HOST_METRICS, VCSIM_HOST_METRICS


@pytest.mark.integration
@pytest.mark.usefixtures("dd_environment")
def test_esxi_metric_up(vcsim_instance, dd_run_check, aggregator):
    check = EsxiCheck('esxi', {}, [vcsim_instance])
    dd_run_check(check)
    aggregator.assert_metric('esxi.host.can_connect', 1, count=1, tags=["esxi_url:127.0.0.1:8989"])


@pytest.mark.integration
@pytest.mark.usefixtures("dd_environment")
def test_esxi_perf_metrics(vcsim_instance, dd_run_check, aggregator, caplog):
    check = EsxiCheck('esxi', {}, [vcsim_instance])
    caplog.set_level(logging.DEBUG)
    dd_run_check(check)

    base_tags = ["esxi_url:127.0.0.1:8989"]
    all_expected_metrics = set(ALL_VCSIM_HOST_METRICS_WITH_VALS) - set(FLAKEY_HOST_METRICS)
    for metric_name in all_expected_metrics:
        aggregator.assert_metric(f"esxi.{metric_name}", tags=base_tags, hostname="localhost.localdomain")

    # some metrics are flakey in the VCSIM env
    for metric_name in FLAKEY_HOST_METRICS:
        aggregator.assert_metric(f"esxi.{metric_name}", at_least=0, tags=base_tags, hostname="localhost.localdomain")

    # assert that the missing metrics are skipped due to missing values
    metrics_without_vals = set(VCSIM_HOST_METRICS) - set(ALL_VCSIM_HOST_METRICS_WITH_VALS) - set(FLAKEY_HOST_METRICS)
    for metric_name in metrics_without_vals:
        log_line = (
            f"Skipping metric {metric_name} for localhost.localdomain because no value was returned by the ESXi host"
        )
        assert log_line in caplog.text

    aggregator.assert_metric("esxi.host.can_connect", 1, count=1, tags=base_tags)
    aggregator.assert_all_metrics_covered()
