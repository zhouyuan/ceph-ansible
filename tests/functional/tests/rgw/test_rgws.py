import pytest


class TestRGWs(object):

    @pytest.mark.no_docker
    def test_rgw_services_are_running(self, node, Service):
        service_name = "ceph-radosgw@rgw.ceph-{hostname}".format(
            hostname=node["vars"]["inventory_hostname"]
        )
        assert Service(service_name).is_running

    @pytest.mark.no_docker
    def test_rgw_services_are_enabled(self, node, Service):
        service_name = "ceph-radosgw@rgw.ceph-{hostname}".format(
            hostname=node["vars"]["inventory_hostname"]
        )
        assert Service(service_name).is_enabled

    @pytest.mark.no_docker
    def test_rgw_http_endpoint(self, node, Interface, Socket):
        # rgw frontends ip_addr is configured on eth0
        ip_addr = Interface("eth0").addresses[0]
        assert Socket("tcp://{ip_addr}:{port}".format(ip_addr=ip_addr, port=8080)).is_listening

