# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

import pytest

from datadog_checks.dev import get_here
from datadog_checks.dev.http import MockResponse

HERE = get_here()


@pytest.fixture(scope="session")
def dd_environment():
    yield


@pytest.fixture
def instance():
    return {"kubevirt_controller_healthz_endpoint": "https://10.244.0.38:443/healthz"}


def mock_http_responses(url, **_params):
    mapping = {
        "https://10.244.0.38:443/healthz": "healthz.txt",
    }

    fixtures_file = mapping.get(url)

    if not fixtures_file:
        raise Exception(f"url `{url}` not registered")

    with open(os.path.join(HERE, "fixtures", fixtures_file)) as f:
        return MockResponse(content=f.read())
