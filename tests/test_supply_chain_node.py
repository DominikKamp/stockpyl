import unittest

# import numpy as np
# from scipy.stats import norm
# from scipy.stats import poisson
# from scipy.stats import lognorm

from pyinv.supply_chain_node import *
from pyinv.instances import *
from pyinv.sim import *


# Module-level functions.

def print_status(class_name, function_name):
	"""Print status message."""
	print("module : test_supply_chain_node   class : {:30s} function : {:30s}".format(class_name, function_name))


def set_up_module():
	"""Called once, before anything else in this module."""
	print_status('---', 'set_up_module()')


def tear_down_module():
	"""Called once, after everything else in this module."""
	print_status('---', 'tear_down_module()')


class TestSupplyChainNodeInit(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestSupplyChainNodeInit', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestSupplyChainNodeInit', 'tear_down_class()')

	# def test_init(self):
	# 	"""Test that SupplyChainNode.__init__() correctly raises errors on
	# 	incorrect parameters.
	# 	"""
	# 	print_status('TestPolicyInit', 'test_init()')


class TestSupplyChainNodeEq(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestSupplyChainNodeEq', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestSupplyChainNodeEq', 'tear_down_class()')

	def test_eq(self):
		"""Test SupplyChainNode.__eq__().
		"""
		print_status('TestSupplyChainNodeEq', 'test_eq()')

		node1 = SupplyChainNode(index=3, name="foo")
		node2 = SupplyChainNode(index=3, name="bar")
		node3 = SupplyChainNode(index=5, name=None)
		node4 = SupplyChainNode(index=5, name="taco")
		node5 = SupplyChainNode(index=3, name="foo")

		eq11 = node1 == node1
		eq12 = node1 == node2
		eq13 = node1 == node3
		eq14 = node1 == node4
		eq15 = node1 == node5
		eq21 = node2 == node1
		eq22 = node2 == node2
		eq23 = node2 == node3
		eq24 = node2 == node4
		eq25 = node2 == node5
		eq31 = node3 == node1
		eq32 = node3 == node2
		eq34 = node3 == node4
		eq35 = node3 == node5

		self.assertEqual(eq11, True)
		self.assertEqual(eq12, True)
		self.assertEqual(eq13, False)
		self.assertEqual(eq14, False)
		self.assertEqual(eq15, True)
		self.assertEqual(eq21, True)
		self.assertEqual(eq22, True)
		self.assertEqual(eq23, False)
		self.assertEqual(eq24, False)
		self.assertEqual(eq25, True)
		self.assertEqual(eq31, False)
		self.assertEqual(eq32, False)
		self.assertEqual(eq34, True)
		self.assertEqual(eq35, False)

	def test_list_contains(self):
		"""Test that a list can correctly determine whether a SupplyChainNode is
		contained in it. This depends on SupplyChainNode.__eq__() working
		properly.
		"""
		print_status('TestSupplyChainNodeEq', 'test_list_contains()')

		node1 = SupplyChainNode(index=3, name="foo")
		node2 = SupplyChainNode(index=3, name="bar")
		node3 = SupplyChainNode(index=5, name=None)
		node4 = SupplyChainNode(index=6, name="taco")
		node5 = SupplyChainNode(index=3, name="foo")

		mylist = [node1, node2, node3]

		contains1 = node1 in mylist
		contains2 = node2 in mylist
		contains3 = node3 in mylist
		contains4 = node4 in mylist
		contains5 = node5 in mylist

		self.assertEqual(contains1, True)
		self.assertEqual(contains2, True)
		self.assertEqual(contains3, True)
		self.assertEqual(contains4, False)
		self.assertEqual(contains5, True)


class TestDescendants(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestDescendants', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestDescendants', 'tear_down_class()')

	def test_example_6_1(self):
		"""Test descendants for 3-node serial system in Example 6.1.
		"""
		print_status('TestDescendants', 'test_example_6_1()')

		network = get_named_instance("example_6_1")

		nodes = network.nodes

		desc = {}
		for i in range(len(nodes)):
			desc[i] = nodes[i].descendants

		self.assertEqual(desc[0], [])
		self.assertEqual(desc[1], [nodes[0]])
		self.assertEqual(desc[2], [nodes[0], nodes[1]])

	def test_4_node_owmr(self):
		"""Test descendants for 4-node OWMR system.
		"""
		print_status('TestDescendants', 'test_4_node_owmr()')

		network = SupplyChainNetwork()

		nodes = []
		for i in range(4):
			nodes.append(SupplyChainNode(i))

		network.add_node(nodes[0])
		network.add_successor(nodes[0], nodes[1])
		network.add_successor(nodes[0], nodes[2])
		network.add_successor(nodes[0], nodes[3])

		desc = {}
		for i in range(len(nodes)):
			desc[i] = nodes[i].descendants

		self.assertEqual(desc[0], [nodes[1], nodes[2], nodes[3]])
		self.assertEqual(desc[1], [])
		self.assertEqual(desc[2], [])
		self.assertEqual(desc[3], [])


class TestAncestors(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestAncestors', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestAncestors', 'tear_down_class()')

	def test_example_6_1(self):
		"""Test ancestors for 3-node serial system in Example 6.1.
		"""
		print_status('TestAncestors', 'test_example_6_1()')

		network = get_named_instance("example_6_1")

		nodes = network.nodes

		anc = {}
		for i in range(len(nodes)):
			anc[i] = nodes[i].ancestors

		self.assertEqual(anc[0], [nodes[1], nodes[2]])
		self.assertEqual(anc[1], [nodes[2]])
		self.assertEqual(anc[2], [])

	def test_4_node_owmr(self):
		"""Test ancestors for 4-node OWMR system.
		"""
		print_status('TestAncestors', 'test_4_node_owmr()')

		network = SupplyChainNetwork()

		nodes = []
		for i in range(4):
			nodes.append(SupplyChainNode(i))

		network.add_node(nodes[0])
		network.add_successor(nodes[0], nodes[1])
		network.add_successor(nodes[0], nodes[2])
		network.add_successor(nodes[0], nodes[3])

		anc = {}
		for i in range(len(nodes)):
			anc[i] = nodes[i].ancestors

		self.assertEqual(anc[0], [])
		self.assertEqual(anc[1], [nodes[0]])
		self.assertEqual(anc[2], [nodes[0]])
		self.assertEqual(anc[3], [nodes[0]])


class TestStateVariables(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestStateVariables', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestStateVariables', 'tear_down_class()')

	def test_example_6_1_per_22(self):
		"""Test state variables for simulation of 3-node serial system in
		Example 6.1 at end of period 22.
		"""
		print_status('TestStateVariables', 'test_example_6_1_per_22()')

		network = get_named_instance("example_6_1")

		# Set initial inventory levels to local BS levels.
		for n in network.nodes:
			n.initial_inventory_level = n.inventory_policy.base_stock_level

		# Strategy for these tests: run sim for a few periods, test state
		# variables.
		simulation(network, 23, rand_seed=17, progress_bar=False)

		self.assertAlmostEqual(network.nodes[0].state_vars[23].on_hand, 0.497397132, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].on_hand, 0.038666224, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].on_hand, 0, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[23].backorders, 0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].backorders, 0, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].backorders, 0.832602868, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].in_transit_to(network.nodes[0]), 5.992602868, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].in_transit_to(network.nodes[1]), 4.658730908, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[23].in_transit_from(network.nodes[1]), 5.992602868, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].in_transit_from(network.nodes[2]), 4.658730908, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].in_transit_from(None), 6.031269092479092+5.491333775514212, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[23].in_transit, 5.992602868, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].in_transit, 4.658730908, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].in_transit, 6.031269092479092+5.491333775514212, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[23].on_order, 5.992602868, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].on_order, 5.491333776, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].on_order, 6.031269092479092+5.491333775514212, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[23].inventory_position, 6.49, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].inventory_position, 5.53, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].inventory_position, 10.69, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[23].echelon_on_hand_inventory, 0.497397132, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].echelon_on_hand_inventory, 0.497397132+5.992602868+0.038666224, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].echelon_on_hand_inventory, 0.497397132+5.992602868+0.038666224+4.658730908, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[23].echelon_inventory_level, 0.497397132, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].echelon_inventory_level, 0.497397132+5.992602868+0.038666224, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].echelon_inventory_level, 0.497397132+5.992602868+0.038666224+4.658730908, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[23].echelon_inventory_position, 0.497397132+5.992602868, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[23].echelon_inventory_position, 0.497397132+5.992602868+0.038666224+5.491333776, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[23].echelon_inventory_position, 0.497397132+5.992602868+0.038666224+4.658730908+6.031269092479092+5.491333775514212, places=6)

	def test_example_6_1_per_37(self):
		"""Test state variables for simulation of 3-node serial system in
		Example 6.1 at end of period 37.
		"""
		print_status('TestStateVariables', 'test_example_6_1_per_37()')

		network = get_named_instance("example_6_1")

		# Set initial inventory levels to local BS levels.
		for n in network.nodes:
			n.initial_inventory_level = n.inventory_policy.base_stock_level

		# Strategy for these tests: run sim for a few periods, test state
		# variables.
		simulation(network, 38, rand_seed=17, progress_bar=False)

		# Shortcuts to correct values.
		[IL0, IL1, IL2] = [-0.16089457,-0.682689274,-0.343065432]
		[OH0, OH1, OH2] = np.maximum([IL0, IL1, IL2], 0)
		[BO0, BO1, BO2] = np.maximum([-IL0, -IL1, -IL2], 0)
		[IT0, IT1, IT2] = [5.968205296, 5.869623842, 5.567783088742498+5.465282343506053]
		[OO0, OO1, OO2] = [6.65089457, 6.212689274, 11.03306543]

		self.assertAlmostEqual(network.nodes[0].state_vars[38].on_hand, OH0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].on_hand, OH1, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].on_hand, OH2, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[38].backorders, BO0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].backorders, BO1, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].backorders, BO2, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].in_transit_to(network.nodes[0]), IT0, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].in_transit_to(network.nodes[1]), IT1, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[38].in_transit_from(network.nodes[1]), IT0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].in_transit_from(network.nodes[2]), IT1, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].in_transit_from(None), IT2, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[38].in_transit, IT0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].in_transit, IT1, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].in_transit, IT2, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[38].on_order, OO0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].on_order, OO1, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].on_order, OO2, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[38].inventory_position, IL0+OO0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].inventory_position, IL1+OO1, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].inventory_position, IL2+OO2, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[38].echelon_on_hand_inventory, OH0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].echelon_on_hand_inventory, OH0+IT0+OH1, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].echelon_on_hand_inventory, OH0+IT0+OH1+IT1+OH2, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[38].echelon_inventory_level, IL0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].echelon_inventory_level, OH0+IT0+OH1-BO0, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].echelon_inventory_level, OH0+IT0+OH1+IT1+OH2-BO0, places=6)
		self.assertAlmostEqual(network.nodes[0].state_vars[38].echelon_inventory_position, IL0+OO0, places=6)
		self.assertAlmostEqual(network.nodes[1].state_vars[38].echelon_inventory_position, OH0+IT0+OH1-BO0+OO1, places=6)
		self.assertAlmostEqual(network.nodes[2].state_vars[38].echelon_inventory_position, OH0+IT0+OH1+IT1+OH2-BO0+OO2, places=6)

