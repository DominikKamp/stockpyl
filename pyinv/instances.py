import copy

from pyinv.supply_chain_network import *


def get_named_instance(instance_name):
	"""Return the named instance specified by ``instance_name``. Return
	variables depend on the instance.

	Parameters
	----------
	instance_name : str
		The instance name. See method code for allowable strings.

	"""

	# CHAPTER 3
	if instance_name == "example_3_1":
		# Example 3.1.
		fixed_cost = 8
		holding_cost = 0.75 * 0.3
		demand_rate = 1300
		return fixed_cost, holding_cost, demand_rate
	elif instance_name == "problem_3_1":
		# Problem 3.1.
		fixed_cost = 2250
		holding_cost = 275
		demand_rate = 500 * 365
		return fixed_cost, holding_cost, demand_rate
	elif instance_name == "example_3_8":
		# Example 3.8.
		fixed_cost = 8
		holding_cost = 0.75 * 0.3
		stockout_cost = 5
		demand_rate = 1300
		return fixed_cost, holding_cost, stockout_cost, demand_rate
	elif instance_name == "problem_3_2b":
		# Problem 3.2(b).
		fixed_cost = 40
		holding_cost = (165 * 0.17 + 12)
		stockout_cost = 60
		demand_rate = 40 * 52
		return fixed_cost, holding_cost, stockout_cost, demand_rate
	elif instance_name == "problem_3_22":
		# Problem 3.22.
		fixed_cost = 4
		holding_cost = 0.08
		demand_rate = 80
		production_rate = 110
		return fixed_cost, holding_cost, demand_rate, production_rate
	elif instance_name == "example_3_9":
		# Example 3.9 (Wagner-Whitin).
		num_periods = 4
		holding_cost = 2
		fixed_cost = 500
		demand = [90, 120, 80, 70]
		return num_periods, holding_cost, fixed_cost, demand
	elif instance_name == "problem_3_27":
		# Problem 3.27.
		num_periods = 4
		holding_cost = 0.8
		fixed_cost = 120
		demand = [150, 100, 80, 200]
		return num_periods, holding_cost, fixed_cost, demand
	elif instance_name == "problem_3_29":
		# Problem 3.29.
		num_periods = 5
		holding_cost = 0.1
		fixed_cost = 100
		demand = [730, 580, 445, 650, 880]
		return num_periods, holding_cost, fixed_cost, demand
	elif instance_name == "ww_hw_c":
		# SCMO HW problem for WW with nonstationary purchase cost.
		num_periods = 5
		holding_cost = 0.1
		fixed_cost = 100
		demand = [400, 500, 500, 1100, 900]
		purchase_cost = [3, 1, 4, 6, 6]
		return num_periods, holding_cost, fixed_cost, demand, purchase_cost
	elif instance_name == "jrp_ex":
		# JRP example in SCMO.
		shared_fixed_cost = 600
		individual_fixed_costs = [120, 840, 300]
		holding_costs = [160, 20, 50]
		demand_rates = [1, 1, 1]
		return shared_fixed_cost, individual_fixed_costs, holding_costs, demand_rates
	elif instance_name == "jrp_hw_1":
		# JRP HW 1 (paper)
		shared_fixed_cost = 20000
		individual_fixed_costs = [36000, 46000, 34000, 38000]
		holding_costs = [1000, 900, 1200, 1000]
		demand_rates = [1780, 445, 920, 175]
		return shared_fixed_cost, individual_fixed_costs, holding_costs, demand_rates
	elif instance_name == "jrp_hw_2":
		# JRP HW 2 (construction)
		shared_fixed_cost = 1500
		individual_fixed_costs = [4000, 1000, 2000]
		holding_costs = [300, 200, 200]
		demand_rates_week = [175, 1600, 400]
		demand_rates = (52 * np.array(demand_rates_week)).tolist()
		return shared_fixed_cost, individual_fixed_costs, holding_costs, demand_rates
	elif instance_name == "jrp_hw_3":
		# JRP HW 3 (books)
		shared_fixed_cost = 180
		individual_fixed_costs = [60, 100, 180, 115, 135]
		purchase_costs = [19, 14, 17, 14, 12]
		holding_costs = (0.28 * np.array(purchase_costs)).tolist()
		demand_rates = [6200, 1300, 400, 4400, 1800]
		return shared_fixed_cost, individual_fixed_costs, holding_costs, demand_rates
	elif instance_name == "jrp_silver":
		# Numerical example in Silver (1976).
		shared_fixed_cost = 10
		individual_fixed_costs = [1.87, 5.27, 7.94, 8.19, 8.87]
		holding_costs = [0.2] * 5
		demand_rates = [1736, 656, 558, 170, 142]
		return shared_fixed_cost, individual_fixed_costs, holding_costs, demand_rates
	elif instance_name == "jrp_spp":
		# Example on p. 428 of Silver, Pyke, and Peterson (1998).
		shared_fixed_cost = 40
		individual_fixed_costs = [15, 15, 15, 15]
		holding_costs = [0.24] * 4
		demand_rates = [86000, 12500, 1400, 3000]
		return shared_fixed_cost, individual_fixed_costs, holding_costs, demand_rates



	# CHAPTER 4
	if instance_name == "example_4_1_network":
		# Example 4.1 (newsvendor), as SupplyChainNetwork object.
		example_4_1_network = serial_system(
			num_nodes=1,
			local_holding_cost=[0.18],
			stockout_cost=[0.70],
			demand_type=DemandType.NORMAL,
			demand_mean=50,
			demand_standard_deviation=8,
			shipment_lead_time=[1],
			inventory_policy_type=InventoryPolicyType.BASE_STOCK,
			local_base_stock_levels=[56.6]
		)
		return example_4_1_network
	elif instance_name == "example_4_1":
		# Example 4.1 (newsvendor).
		holding_cost = 0.18
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8
		return holding_cost, stockout_cost, demand_mean, demand_sd
	elif instance_name == "example_4_3":
		# Example 4.3 (= Example 4.1).
		return get_named_instance("example_4_1")
	elif instance_name == "problem_4_1":
		# Problem 4.1.
		holding_cost = 65-22
		stockout_cost = 129-65+15
		demand_mean = 900
		demand_sd = 60
		return holding_cost, stockout_cost, demand_mean, demand_sd
	elif instance_name == "example_4_4":
		# Example 4.4.
		holding_cost = 0.18
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8
		lead_time = 4
		return holding_cost, stockout_cost, demand_mean, demand_sd, lead_time
	elif instance_name == "example_4_7":
		# Example 4.7 (Poisson).
		holding_cost = 1
		stockout_cost = 4
		demand_mean = 6
		fixed_cost = 5
		return holding_cost, stockout_cost, fixed_cost, demand_mean
	elif instance_name == "problem_4_8a":
		# Problem 4.8(a).
		holding_cost = 200
		stockout_cost = 270
		demand_mean = 18
		return holding_cost, stockout_cost, demand_mean
	elif instance_name == "problem_4_7b":
		# Problem 4.7(b).
		holding_cost = 500000
		stockout_cost = 1000000
		demand_pmf = {1: 0.25, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.15, 6: 0.10, 7: 0.10, 8: 0.05}
		return holding_cost, stockout_cost, demand_pmf
	elif instance_name == "problem_4_8b":
		# Problem 4.8(b) -- lognormal newsvendor.
		holding_cost = 1
		stockout_cost = 0.1765
		mu = 6
		sigma = 0.3
		return holding_cost, stockout_cost, mu, sigma
	elif instance_name == "problem_4_31":
		# Problem 4.31.
		holding_cost = 40
		stockout_cost = 125
		fixed_cost = 150
		demand_mean = 4
		return holding_cost, stockout_cost, fixed_cost, demand_mean
	elif instance_name == "example_4_8":
		# Example 4.8 (= Example 4.4 + K = 2.5).
		holding_cost, stockout_cost, demand_mean, demand_sd, _ = \
			get_named_instance("example_4_4")
		fixed_cost = 2.5
		return holding_cost, stockout_cost, fixed_cost, demand_mean, demand_sd
	elif instance_name == "problem_4_32":
		# Problem 4.32.
		holding_cost = 2
		stockout_cost = 36
		fixed_cost = 60
		demand_mean = 190
		demand_sd = 48
		return holding_cost, stockout_cost, fixed_cost, demand_mean, demand_sd
	elif instance_name == "problem_4_29":
		# Problem 4.29.
		num_periods = 10
		holding_cost = 1
		stockout_cost = 25
		terminal_holding_cost = holding_cost
		terminal_stockout_cost = stockout_cost
		purchase_cost = 1
		fixed_cost = 0
		demand_mean = 18
		demand_sd = 3
		discount_factor = 0.98
		initial_inventory_level = 0
		return num_periods, holding_cost, stockout_cost, terminal_holding_cost, \
			terminal_stockout_cost, purchase_cost, fixed_cost, demand_mean, \
			demand_sd, discount_factor, initial_inventory_level
	elif instance_name == "problem_4_30":
		# Problem 4.30 (= Problem 4.29 + fixed_cost = 40).
		num_periods, holding_cost, stockout_cost, terminal_holding_cost, \
			terminal_stockout_cost, purchase_cost, _, demand_mean, \
			demand_sd, discount_factor, initial_inventory_level = \
			get_named_instance("problem_4_29")
		fixed_cost = 40
		return num_periods, holding_cost, stockout_cost, terminal_holding_cost, \
			terminal_stockout_cost, purchase_cost, fixed_cost, demand_mean, \
			demand_sd, discount_factor, initial_inventory_level

	# CHAPTER 5
	if instance_name == "example_5_1":
		# Example 5.1 (plus 5.2-5.6).
		holding_cost = 0.225
		stockout_cost = 7.5
		fixed_cost = 8
		demand_mean = 1300
		demand_sd = 150
		lead_time = 1/12
		return holding_cost, stockout_cost, fixed_cost, demand_mean, demand_sd, lead_time
	elif instance_name == "problem_5_1":
		# Problem 5.1.
		holding_cost = 3.1
		stockout_cost = 45
		fixed_cost = 50
		demand_mean = 800
		demand_sd = 40
		lead_time = 4/365
		return holding_cost, stockout_cost, fixed_cost, demand_mean, demand_sd, lead_time
	elif instance_name == "problem_5_3":
		# Problem 5.3.
		holding_cost = 1.5 / 7
		stockout_cost = 40
		fixed_cost = 85
		demand_mean = 192
		demand_sd = 17.4
		lead_time = 3
		return holding_cost, stockout_cost, fixed_cost, demand_mean, demand_sd, lead_time
	elif instance_name == "example_5_8":
		# Example 5.8 (Poisson).
		holding_cost = 20
		stockout_cost = 150
		fixed_cost = 100
		demand_mean = 1.5
		lead_time = 2
		return holding_cost, stockout_cost, fixed_cost, demand_mean, lead_time
	elif instance_name == "problem_5_2":
		# Problem 5.2.
		holding_cost = 4
		stockout_cost = 28
		fixed_cost = 4
		demand_mean = 12
		lead_time = 0.5
		return holding_cost, stockout_cost, fixed_cost, demand_mean, lead_time

	# CHAPTER 6
	if instance_name == "example_6_1":
		# Example 6.1.
		example_6_1_network = serial_system(
			num_nodes=3,
			local_holding_cost=[7, 4, 2],
			echelon_holding_cost=[3, 2, 2],
			stockout_cost=[37.12, 0, 0],
			demand_type=DemandType.NORMAL,
			demand_mean=5,
			demand_standard_deviation=1,
			shipment_lead_time=[1, 1, 2],
			inventory_policy_type=InventoryPolicyType.BASE_STOCK,
			local_base_stock_levels=[6.49, 5.53, 10.69],
			downstream_0=True
		)
		return example_6_1_network
	elif instance_name == "problem_6_1":
		# Problem 6.1.
		problem_6_1_network = serial_system(
			num_nodes=2,
			local_holding_cost=[2, 1],
			echelon_holding_cost=[1, 1],
			stockout_cost=[15, 0],
			demand_type=DemandType.NORMAL,
			demand_mean=100,
			demand_standard_deviation=15,
			shipment_lead_time=[1, 1],
			inventory_policy_type=InventoryPolicyType.BASE_STOCK,
			local_base_stock_levels=[100, 94],
			downstream_0=True
		)
		return problem_6_1_network
	elif instance_name == "problem_6_2a":
		# Problem 6.2a.
		problem_6_2a_network = serial_system(
			num_nodes=5,
			local_holding_cost=[1, 2, 3, 5, 7],
			echelon_holding_cost=[2, 2, 1, 1, 1],
			stockout_cost=[24, 0, 0, 0, 0],
			demand_type=DemandType.NORMAL,
			demand_mean=64,
			demand_standard_deviation=8,
			shipment_lead_time=[0.5, 0.5, 0.5, 0.5, 0.5],
			inventory_policy_type=InventoryPolicyType.BASE_STOCK,
			local_base_stock_levels=[40.59, 33.87, 35.14, 33.30, 32.93],
			downstream_0=True
		)
		return problem_6_2a_network
	elif instance_name == "problem_6_2a_adj":
		# Problem 6.2a, adjusted for periodic review.
		# (Since L=0.5 in that problem, here we treat each period as
		# having length 0.5 in the original problem.)
		problem_6_2a_network_adj = serial_system(
			num_nodes=5,
			local_holding_cost=list(np.array([1, 2, 3, 5, 7]) / 2),
			stockout_cost=list(np.array([24, 0, 0, 0, 0]) / 2),
			demand_type=DemandType.NORMAL,
			demand_mean=64 / 2,
			demand_standard_deviation=8 / np.sqrt(2),
			shipment_lead_time=[1, 1, 1, 1, 1],
			inventory_policy_type=InventoryPolicyType.BASE_STOCK,
			local_base_stock_levels=[40.59, 33.87, 35.14, 33.30, 32.93],
			downstream_0=True
		)
		return problem_6_2a_network_adj
	elif instance_name == "problem_6_2b_adj":
		# Problem 6.2b, adjusted for periodic review.
		# (Since L=0.5 in that problem, here we treat each period as
		# having length 0.5 in the original problem.)
		problem_6_2b_network_adjusted = copy.deepcopy(problem_6_2a_network_adj)
		# TODO: build this instance - -need to add Poisson demand capability
		return problem_6_2b_network_adjusted
	elif instance_name == "problem_6_16":
		# Problem 6.16.
		problem_6_16_network = serial_system(
			num_nodes=2,
			local_holding_cost=[7, 2],
			stockout_cost=[24, 0],
			demand_type=DemandType.NORMAL,
			demand_mean=20,
			demand_standard_deviation=4,
			shipment_lead_time=[8, 3],
			inventory_policy_type=InventoryPolicyType.BASE_STOCK,
			local_base_stock_levels=[171.1912, 57.7257],
			initial_IL=20,
			initial_orders=20,
			initial_shipments=20,
			downstream_0=True
		)
		return problem_6_16_network

	# INSTANCES NOT FROM TEXTBOOK
	if instance_name == "assembly_3_stage":
		assembly_3_stage_network = mwor_system(
			num_warehouses=2,
			local_holding_cost=[2, 1, 1],
			stockout_cost=[20, 0, 0],
			demand_type=DemandType.NORMAL,
			demand_mean=5,
			demand_standard_deviation=1,
			shipment_lead_time=[1, 2, 2],
			inventory_policy_type=InventoryPolicyType.LOCAL_BASE_STOCK,
			local_base_stock_levels=[7, 13, 11],
			initial_IL=[7, 13, 11],
			downstream_0=True
		)
		assembly_3_stage_network.nodes[0].demand_source.round_to_int = True
		return assembly_3_stage_network
	elif instance_name == "assembly_3_stage_2":
			assembly_3_stage_2_network = network_from_edges(
				edges=[(1, 3), (2, 3)],
				local_holding_cost={1: 1, 2: 1, 3: 2},
				stockout_cost={1: 0, 2: 0, 3: 20},
				demand_type={1: DemandType.NONE, 2: DemandType.NONE, 3: DemandType.NORMAL},
				demand_mean=20,
				demand_standard_deviation=5,
				shipment_lead_time={1: 2, 2: 2, 3: 1},
				inventory_policy_type=InventoryPolicyType.LOCAL_BASE_STOCK,
				local_base_stock_levels={1: 44, 2: 52, 3: 28},
				initial_IL={1: 44, 2: 52, 3: 28}
			)
			# assembly_3_stage_2_network = mwor_system(
			# 	num_warehouses=2,
			# 	local_holding_cost=[2, 1, 1],
			# 	stockout_cost=[20, 0, 0],
			# 	demand_type=DemandType.NORMAL,
			# 	demand_mean=20,
			# 	demand_standard_deviation=5,
			# 	shipment_lead_time=[1, 2, 2],
			# 	inventory_policy_type=InventoryPolicyType.LOCAL_BASE_STOCK,
			# 	local_base_stock_levels=[28, 52, 44],
			# 	initial_IL=[28, 52, 44],
			# 	downstream_0=True)
			assembly_3_stage_2_network.get_node_from_index(3).demand_source.round_to_int = True
			return assembly_3_stage_2_network
	elif instance_name == "rosling_figure_1":
		# Figure 1 from Rosling (1989).
		# Note: Other than the structure and lead times, none of the remaining parameters are from Rosling's paper.
		rosling_figure_1_network = SupplyChainNetwork()
		nodes = {i: SupplyChainNode(index=i) for i in range(1, 8)}
		demand_source_factory = DemandSourceFactory()
		policy_factory = PolicyFactory()
		# Inventory policies.
		for n in nodes.values():
			policy = policy_factory.build_policy(InventoryPolicyType.BALANCED_ECHELON_BASE_STOCK,
												 base_stock_level=None)
			n.inventory_policy = policy
		# Node 1.
		nodes[1].shipment_lead_time = 1
		demand_source = demand_source_factory.build_demand_source(DemandType.UNIFORM_DISCRETE)
		demand_source.lo = 0
		demand_source.hi = 10
		nodes[1].demand_source = demand_source
		nodes[1].supply_type = SupplyType.NONE
		nodes[1].inventory_policy.echelon_base_stock_level = 8
		nodes[1].initial_inventory_level = 8
		rosling_figure_1_network.add_node(nodes[1])
		# Node 2.
		nodes[2].shipment_lead_time = 1
		nodes[2].supply_type = SupplyType.NONE
		nodes[2].inventory_policy.echelon_base_stock_level = 24
		nodes[2].initial_inventory_level = 8
		rosling_figure_1_network.add_predecessor(nodes[1], nodes[2])
		# Node 3.
		nodes[3].shipment_lead_time = 3
		nodes[3].supply_type = SupplyType.NONE
		nodes[3].inventory_policy.echelon_base_stock_level = 40
		nodes[3].initial_inventory_level = 24
		rosling_figure_1_network.add_predecessor(nodes[1], nodes[3])
		# Node 4.
		nodes[4].shipment_lead_time = 2
		nodes[4].supply_type = SupplyType.NONE
		nodes[4].inventory_policy.echelon_base_stock_level = 76
		nodes[4].initial_inventory_level = 16
		rosling_figure_1_network.add_predecessor(nodes[3], nodes[4])
		# Node 5.
		nodes[5].shipment_lead_time = 4
		nodes[5].inventory_policy.echelon_base_stock_level = 62
		nodes[5].initial_inventory_level = 32
		nodes[5].supply_type = SupplyType.UNLIMITED
		rosling_figure_1_network.add_predecessor(nodes[2], nodes[5])
		# Node 6.
		nodes[6].shipment_lead_time = 1
		nodes[6].supply_type = SupplyType.UNLIMITED
		nodes[6].inventory_policy.echelon_base_stock_level = 84
		nodes[6].initial_inventory_level = 8
		rosling_figure_1_network.add_predecessor(nodes[4], nodes[6])
		# Node 7.
		nodes[7].shipment_lead_time = 2
		nodes[7].supply_type = SupplyType.UNLIMITED
		nodes[7].inventory_policy.echelon_base_stock_level = 92
		nodes[7].initial_inventory_level = 16
		rosling_figure_1_network.add_predecessor(nodes[4], nodes[7])
		return rosling_figure_1_network
	elif instance_name == "kangye_4_stage":
		kangye_4_stage = mwor_system(
			num_warehouses=3,
			demand_type=DemandType.NORMAL,
			demand_mean=20,
			demand_standard_deviation=4,
			shipment_lead_time=[1, 1, 2, 3],
			inventory_policy_type=InventoryPolicyType.BALANCED_ECHELON_BASE_STOCK,
			echelon_base_stock_levels=[30, 50, 70, 90],
			downstream_0=True
		)
		return kangye_4_stage
	elif instance_name == "kangye_3_stage_serial":
		kangye_3_stage_serial = serial_system(
			num_nodes=3,
			local_holding_cost=[1, 5, 10],
			stockout_cost=[0, 0, 100],
			demand_type=DemandType.NORMAL,
			demand_mean=5,
			demand_standard_deviation=np.sqrt(5),
			shipment_lead_time=[1, 1, 1],
			inventory_policy_type=InventoryPolicyType.BASE_STOCK,
			local_base_stock_levels=[7, 7, 7],
			initial_IL=[7, 7, 7],
			downstream_0=False
		)
		for i in range(2):
			kangye_3_stage_serial.get_node_from_index(i).in_transit_holding_cost = 0
		kangye_3_stage_serial.get_node_from_index(2).demand_source.round_to_int = True
		return kangye_3_stage_serial
	elif instance_name == "michelle_sean_3_stage":
		michelle_sean_3_stage = mwor_system(
			num_warehouses=2,
			demand_type=DemandType.NORMAL,
			demand_mean=50,
			demand_standard_deviation=10,
			local_holding_cost=[10, 10, 10],
			stockout_cost=[10, 10, 10],
			shipment_lead_time=[1, 1, 1],
			inventory_policy_type=InventoryPolicyType.LOCAL_BASE_STOCK,
			local_base_stock_levels=[60, 50, 60],
			downstream_0=True,
			initial_IL=[60, 50, 60]
		)
		return michelle_sean_3_stage
	elif instance_name == "rong_atan_snyder_figure_1a":
		# Uses normal demand instead of Poisson.
		# TODO: add costs and lead times
		rong_atan_snyder_figure_1a = network_from_edges(
			edges=[(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)],
			demand_type={0: DemandType.NONE, 1: DemandType.NONE, 2: DemandType.NONE, 3: DemandType.NORMAL, 4: DemandType.NORMAL, 5: DemandType.NORMAL, 6: DemandType.NORMAL},
			demand_mean=8,
			demand_standard_deviation=np.sqrt(8),
			local_holding_cost={0: 1/3, 1: 2/3, 2: 2/3, 3: 1, 4: 1, 5: 1, 6: 1},
			stockout_cost=20,
			shipment_lead_time=1,
			inventory_policy_type=InventoryPolicyType.LOCAL_BASE_STOCK,
			local_base_stock_levels={i: 0 for i in range(0, 7)}
		)
		return rong_atan_snyder_figure_1a
	elif instance_name == "rong_atan_snyder_figure_1b":
		# Uses normal demand instead of Poisson.
		# TODO: add costs and lead times
		demand_type = {i: DemandType.NORMAL if i >= 3 else DemandType.NONE for i in range(11)}
		rong_atan_snyder_figure_1b = network_from_edges(
			edges=[(0, 1), (0, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 8), (2, 9), (2, 10)],
			demand_type=demand_type,
			demand_mean=8,
			demand_standard_deviation=np.sqrt(8),
			inventory_policy_type=InventoryPolicyType.LOCAL_BASE_STOCK,
			local_base_stock_levels={i: 0 for i in range(0, 11)}
		)
		return rong_atan_snyder_figure_1b
	elif instance_name == "rong_atan_snyder_figure_1c":
		# Uses normal demand instead of Poisson.
		# TODO: add costs and lead times
		rong_atan_snyder_figure_1c = network_from_edges(
			edges=[(0, 1), (0, 2), (2, 3), (2, 4), (2, 5)],
			demand_type={0: DemandType.NONE, 1: DemandType.NORMAL, 2: DemandType.NONE, 3: DemandType.NORMAL, 4: DemandType.NORMAL, 5: DemandType.NORMAL},
			demand_mean=8,
			demand_standard_deviation=np.sqrt(8),
			inventory_policy_type=InventoryPolicyType.LOCAL_BASE_STOCK,
			local_base_stock_levels={i: 0 for i in range(0, 6)}
		)
		return rong_atan_snyder_figure_1c
