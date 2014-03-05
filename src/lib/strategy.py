#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" ==================================================================================================
    strategy.py - A Strategy object encodes a discrete strategy, which gives a system move in response
    to an environment move (or the reverse, in the case of a counterstrategy).
    ==================================================================================================
"""

import math
import re

# TODO: always references states as objects, always use bool types
# TODO: separate out execution code?
# TODO: allow mopsy usage cleanly
# TODO: make f/s adjustments easy in the future, somehow?
# TODO: minimize interdependence so constantine can use
# TODO: classmethod constructor that creates correct subclass based on filename

class Domain:
    """
    A Domain is a bit-vector abstraction, allowing a proposition to effectively have values other than
    just True and False.

    Domain "x" consists of propositions "x_b0", "x_b1", "x_b2", ..., and the value of the domain corresponds
    to the interpretation of these propositions as a binary string (following the order specified
    by `endianness`).  If `value_mapping` is specified, the numeric value of the domain will be used
    as an index into this array, and the corresponding element (must be non-integer) will be returned when the proposition value
    is queried, instead of a number (likewise, when setting the value of the proposition, this mapping will be
    used in reverse).

    `num_props` can be used to specify the size of the vector; if not specified,
    this will be automatically calculated based on the size of the `value_mapping` array.
    """

    B0_IS_MSB, B0_IS_LSB = range(2)

    def __init__(self, name, endianness=B0_IS_MSB, value_mapping=None, num_props=None):
        if not re.match(r"^[A-Za-z][A-Za-z0-9_]*$", name):
            raise ValueError("Name must begin with a letter and contain only alphanumeric characters or underscores.")

        self.name = name

        if endianness not in [Domain.B0_IS_MSB, Domain.B0_IS_LSB]:
            raise ValueError("Invalid endianness: choose either B0_IS_MSB or B0_IS_LSB.")
        self.endianness = endianness

        self.value_mapping = value_mapping
        if num_props is None:
            if value_mapping is None:
                raise TypeError("Cannot create domain without either value_mapping or num_props specified.")
            else:
                self.num_props = max(1,int(math.ceil(math.log(len(value_mapping),2))))
        else:
            self.num_props = num_props

    def propAssignmentsToValue(self, prop_assignments):
        """ Return the value of this domain, based on a dictionary [prop_name(str)->value(bool)] of 
            the values of the propositions composing this domain.
        """
        n = self.propAssignmentsToNumericValue(prop_assignments)

        if self.value_mapping is None:
            return n
        else:
            return self.value_mapping[n]

    def propAssignmentsToNumericValue(self, prop_assignments):
        """ Convert a dictionary [prop_name(str)->value(bool)] of propositions composing this domain
            into an integer value.
        """

        value = 0
        for bit in range(self.num_props):
            if prop_assignments["{}_b{}".format(self.name, bit)]:
                if self.endianness == Domain.B0_IS_MSB:
                    value += 2**((self.num_props-1)-bit)
                else:
                    value += 2**(bit-1)

        return value

    def valueToPropAssignments(self, value):
        """ Convert a value into the corresponding dictionary [prop_name(str)->value(bool)]
            of propositions composing this domain
        """

        if isinstance(value, int) or self.value_mapping is None:
            n = value
        else:
            n = self.value_mapping.index(value)

        return self.numericValueToPropAssigments(n)

    def numericValueToPropAssigments(self, number):
        """ Convert an integer value into the corresponding dictionary [prop_name(str)->value(bool)]
            of propositions composing this domain
        """
        if not isinstance(number, int):
            raise TypeError("Cannot set domain to non-integral value.")
        if number < 0:
            raise TypeError("Cannot set domain to negative value.")
        
        bs = "{0:0>{1}}".format(bin(number)[2:], self.num_props)

        return {"{}_b{}".format(self.name, bit):(v=="1") for bit, v in 
                enumerate(bs if self.endianness == Domain.B0_IS_MSB else reversed(bs))} 

    def __str__(self):
        return '<Domain "{0}" ({0}_b0:{0}_b{1})>'.format(self.name, self.num_props-1)

class State:
    """
    At its most basic, a state has only binary proposition values (this is
    stored internally as the set of propositions that are true in the state);
    more information can be attached by subclasses

    When created, a reference to the parent StateCollection needs to be be
    passed so that the state is aware of its evaluation context
    """
    
    def __init__(self, parent, true_props):
        if not isinstance(parent, StateCollection):
            raise TypeError("The parent of a State must be a StateCollection.")

        self.context = parent
        self.true_props = frozenset(true_props) # set of names of propositions that are true in this state

    def getInputs(self, eval_domains=True):
        """ Return a dictionary of input proposition values for this state.

            If `eval_domains` is True, ignore individual bit-vector propositions and return only the value of
            the relevant domain in its entirety. """
        if eval_domains:
            pass #TODO
        else:
            return self.getPropValues(self.context.input_props)

    def getOutputs(self, eval_domains=True):
        return self.getPropValues(self.context.output_props, eval_domains)

    def getAll(self, eval_domains=True):
        return self.getPropValues(self.context.input_props + self.context.output_props, eval_domains)

    def getPropValues(self, names, eval_domains=True):
        return {p:self.getPropValue(p, eval_domains) for p in names} 

    def getDomainValue(self, name):
        d = self.context.getDomainByName(name)
        return d.propAssignmentsToValue(self.getAll(eval_domains=False))

    def getPropValue(self, name):
        # Check to see if a domain with this name exists
        if prop_name in domains:
            return self.getDomainValue(prop_name)
        else:
            return self.prop_values[prop_name]

    def setPropValues(self, prop_assignments):
        # TOOD: warning
        pass

    def __eq__(self, other):
        return (self.context is other.context) and (self.true_props == other.true_props)

    def __str__(self):
        return "<State with assignment: inputs = {}, outputs = {}>".format(self.getInputs(), self.getOutputs())

class StateCollection(list):
    """
    StateCollection is a simple extension of list, to allow for keeping track of
    meta-information about states, such as which propositions are inputs and which
    are outputs, as well as domains. (These are not class properties of State
    because different StateCollections might have different settings.)
    """
    def __init__(self, *args, **kwds):
        self.input_props = []
        self.output_props = []
        self.domains = []#[Domain("region", Domain.B0_IS_MSB, regions)]
        super(StateCollection, self).__init__(*args, **kwds)

    def addState(self, ...)
    def getDomainOfProp(self, prop_name):

    def getDomainByName(self, name):
        for d in self.domains:
            if d.name == name:
                return d

        raise ValueError("No domain defined with name '{}'".format(name))

class Strategy:
    """
    An automaton object is a collection of state objects along with information about the
    current state of the automaton when being executed.
    """
    def __init__ (self, proj):
        """
        Creates a new automaton.

        You need to pass project instance
        """

        self.proj = proj

        self.states = []    # A collection of state objects belonging to the automaton

        self.regions = proj.rfi.regions # a list of region objects
        self.regionMapping = proj.regionMapping # mapping between original regions and decomposed regions
        self.num_bits = int(numpy.ceil(numpy.log2(len(self.regions))))  # Number of bits necessary to encode all regions

        # Store references to the handlers
        self.sensor_handler = proj.sensor_handler # handler objects for sensors
        self.actuator_handler = proj.actuator_handler # handler objects for actuators
        if proj.h_instance is not None:
            # for view automaton and mopsy, h_instance is None
            self.motion_handler = proj.h_instance['motionControl'] # region-to-region movement handler
        else:
            self.motion_handler = None
        self.h_instance = proj.h_instance

        self.initialize()

    def initialize(self):
        # Variables for keeping track of the current state
        self.current_state = None
        self.current_region = None
        self.current_outputs = {}
        self.arrived = False

    def stateWithName(self, name):
        """
        Find the state with the given name
        """
        for i in range(len(self.states)):
            if(self.states[i].name == name):
                return self.states[i]

        print "ERROR: Can't find state with name %s!" % (name)
        return None

    def dumpStates(self, range=None):
        """
        Print out the contents of the automaton in a human-readable format
        """
        if range is None:
            range = self.states

        for state in range:
            print "Name: ", state.name
            print "Inputs: "
            for key, val in state.inputs.iteritems():
                print key + " = " + val
            print "Outputs: "
            for key, val in state.outputs.iteritems():
                print key + " = " + val
            print "Transitions: "
            for trans in state.transitions:
                print trans.name

    def updateOutputs(self, state=None):
        """
        Update the values of current outputs in our execution environment to reflect the output
        proposition values associated with the given state
        """

        if state is None:
            state = self.current_state

        for key, output_val in state.outputs.iteritems():
            # Skip any "bitX" region encodings
            if re.match('^bit\d+$', key): continue

            new_val = (output_val == "1")

            if key not in self.current_outputs or new_val != self.current_outputs[key]:
                # The state of this output proposition has changed!

                print "Output proposition \"%s\" is now %s!" % (key, str(new_val))

                # Run any actuator handlers if appropriate
                if key in self.actuators:
                    self.motion_handler.gotoRegion(self.current_region, self.current_region)  # Stop, in case actuation takes time
                    #self.actuator_handler.setActuator(key, new_val)
                    initial=False
                    exec(self.actuator_handler[key])

                self.current_outputs[key] = new_val

    def regionFromState(self, state):
        """
        Given a state object, look at its 'bitX' outputs to determine the region encoded,
        and return the NUMBER of this region.
        """
        try:
            region = 0
            for bit in range(self.num_bits):
                if (int(state.outputs["bit" + str(bit)]) == 1):
                    # bit0 is MSB
                    region += int(2**(self.num_bits-bit-1))
        except KeyError:
            print "FATAL: Missing expected proposition 'bit%d' in automaton!" % bit
            region = None

        return region

    def loadFile(self, filename, sensors, actuators, custom_props):
        """
        Create an automaton by reading in a file produced by TLV.

        In addition to a filename, you also need to provide a list of sensor names (so that we can tell the difference between system and environment propositions when reading the file), and a list of actuator names (so we can distinguish internal state propositions from outputs).

        Basically just a lot of regexes.
        """
        # Clear any existing states
        self.states = []
        self.initialize()

        # These will be used later by updateOutputs() and findTransitionableState()
        self.actuators = actuators
        self.sensors = sensors
        self.custom_props = custom_props

        FILE = open(filename,"r")
        fsa_description = FILE.read()
        FILE.close()

        ###################
        # Read in states: #
        ###################

        # A magical regex to slurp up a state and its information all at once
        p = re.compile(r"State (?P<num>\d+) with rank (?P<rank>[\d\(\),-]+) -> <(?P<conds>(?:\w+:\d(?:, )?)+)>", re.IGNORECASE|re.MULTILINE)
        self.last_next_states = []
        self.next_state = None
        self.next_region = None
        m = p.finditer(fsa_description)

        # Now, for each state we find:
        for match in m:

            # Get the number (at least the number that TLV assigned the state; TLV deletes states
            # during optimization, resulting in non-consecutive numbering which would be bad for binary
            # encoding efficiency, so we don't use these numbers internally except as state names)
            # and rank (an irrelevant synthesis byproduct that we only read in for completeness).
            # This is the easy part.

            number = match.group('num')
            rank = match.group('rank')

            # A regex so we can iterate over "PROP = VALUE" terms
            p2 = re.compile(r"(?P<var>\w+):(?P<val>\d)", re.IGNORECASE|re.MULTILINE)
            m2 = p2.finditer(match.group('conds'))

            inputs = {}
            outputs = {}

            # So, for each of these terms:
            for new_condition in m2:
                var = new_condition.group('var')
                val = new_condition.group('val')

                # And then put it in the right place!

                if var not in sensors:
                    # If it's not a sensor proposition, then it's an output proposition
                    outputs[var]=val
                else:
                    # Oh hey it's a sensor
                    inputs[var]=val

            # We'll add transitions later; first we have to create all the states so we can
            # refer to them when we define transitions
            transitions = []

            # Create the state and add it to our collection
            newstate = FSA_State(number, inputs, outputs, transitions)
            newstate.rank=rank
            self.states.append(newstate)


        ########################
        # Read in transitions: #
        ########################

        # Another simple regex, this time for reading in transition definitions
        p = re.compile(r"State (?P<start>\d+)[^\n]+\s*With successors : (?P<ends>(?:\d+(?:, )?)+)", re.IGNORECASE|re.MULTILINE)
        m = p.finditer(fsa_description)

        # For each line:
        for match in m:
            # Get the state that the transitions come FROM
            start = match.group('start')
            # And make a list of the states that the transitions go TO
            ends = match.group('ends').split(', ')

            # Change the references to state names into references to the corresponding state objects
            ends = map(lambda name: self.stateWithName(name), ends)

            # Stick these transitions onto the appropriate state
            self.stateWithName(start).transitions = ends

        # All done, hooray!
        print "Loaded %d states." % len(self.states)
        #self.dumpStates()

        # Check that all necessary sensor and acuator handlers are present
        if self.sensor_handler is None:
            # We won't be executing anyways
            return True

        for sensor in self.sensors:
            if sensor not in self.sensor_handler:
                print "ERROR: No sensor proposition mapping exists for '%s'! Aborting." % sensor
                return False

        for actuator in self.actuators:
            if actuator not in self.actuator_handler:
                print "ERROR: No actuator proposition mapping exists for '%s'! Aborting." % actuator
                return False

        return True

    def getAnnotatedRegionName(self, region_num):
        # annotate any pXXX region names with their human-friendly name
        # convert to set to avoid infinite explosion
        text = self.regions[region_num].name
        for p_reg in set(re.findall(r'\b(p\d+)\b',text)):
            for rname, subregs in self.regionMapping.iteritems():
                if p_reg in subregs:
                    break
            text = re.sub(r'\b'+p_reg+r'\b', '%s (%s)' % (p_reg, rname), text)

        return text

    def writeDot(self, filename):
        """
        Write a dot file so we can look at the automaton visually.
        """

        FILE = open(filename,"w")

        # Write the header
        FILE.write('digraph A { \n')
        FILE.write('\trankdir=LR;\n')
        #FILE.write('\tratio = 0.75;\n')
        FILE.write('\tsize = "8.5,11";\n')
        FILE.write('\toverlap = false;\n')
        #FILE.write('\tlayout = hierarchical;\n')

        # Write the states with region and outputs that are true
        for state in self.states:
            FILE.write('\ts'+ state.name + ' [style=\"bold\",width=0,height=0, fontsize = 20, label=\"')
            stateRegion = self.regionFromState(state)
            FILE.write( self.getAnnotatedRegionName(stateRegion) + '\\n')
            for key in state.outputs.keys():
                if re.match('^bit\d+$',key): continue
                if state.outputs[key] == '1':
                    FILE.write( key + '\\n')
                else:
                    FILE.write( '�' + key + '\\n')
            #FILE.write( "("+state.rank + ')\\n ')
            FILE.write('\" ];\n')

        # Write the transitions with the input labels (only inputs that are true)
        for state in self.states:
            for nextState in state.transitions:
                FILE.write('\ts'+ state.name +' -> s'+ nextState.name +'[style=\"bold\", arrowsize = 1.5, fontsize = 20, label=\"')
                # Check the next state to figure out which inputs have to be on
                for key in nextState.inputs.keys():
                    if nextState.inputs[key] == '1':
                        FILE.write( key + '\\n')
                    else:
                        FILE.write( '�' + key + '\\n')
                FILE.write('\" ];\n')

        FILE.write('} \n')
        FILE.close()

    def findTransitionableStates(self, initial=False):
        """
        Returns a list of states that we could conceivably transition to, given
        the environment state (determined by querying the sensor handler)

        If ``initial`` is true, the current region and output propositions will constrain
        state selection as well.
        """

        candidates = []

        # Define our pool of states to select from
        if initial:
            state_list = self.states

            # initialize all sensor and actuators
            for prop,codes in self.sensor_handler['initializing_handler'].iteritems():
                if prop in self.sensors:
                    for code in codes:
                        eval(code, {'self':self,'initial':True})
            for prop,codes in self.actuator_handler['initializing_handler'].iteritems():
                if prop in self.actuators:
                    new_val = self.current_outputs[prop]
                    for code in codes:
                        eval(code, {'self':self,'initial':True,'new_val':new_val})
        else:
            state_list = self.current_state.transitions

        # Take a snapshot of our current sensor readings
        # This is so we don't risk the readings changing in the middle of our state search
        sensor_state = {}
        for sensor in self.sensors:
            sensor_state[sensor] = eval(self.sensor_handler[sensor], {'self':self,'initial':False})

        for state in state_list:
            okay = True

            if initial:
                # First see if we can be in the state given our current region
                if self.regionFromState(state) != self.current_region: continue
                
                # Start only with Rank 0 states
                #if int(state.rank) != 0: continue

                # Now check whether our current output values match those of the state
                for key, value in state.outputs.iteritems():
                    # Ignore "bitX" output propositions
                    if re.match('^bit\d+$', key): continue

                    if int(self.current_outputs[key]) != int(value):
                        okay = False
                        break

                if not okay: continue

            # Now check whether our current sensor values match those of the state
            for key, value in state.inputs.iteritems():
                if int(sensor_state[key]) != int(value):
                    okay = False
                    break

            if okay:
                candidates.append(state)

        return candidates

    def chooseInitialState(self, init_region, init_outputs):
        """
        Search through all our states to find one that satisfies our current system and environment states,
        so that we may begin our execution from there.

        * ``init_region`` is the number of our starting region
        * ``init_outputs`` is a list of output proposition names that are TRUE initially.
        """

        self.current_region = init_region

        for output in (self.actuators + self.custom_props):
            self.current_outputs[output] = (output in init_outputs)

        candidates = self.findTransitionableStates(initial=True)

        if len(candidates) == 0: # Uh oh; that's no good
            print "(FSA) OH NO, where do I start?! (No suitable initial state found)"
            return None

        # If there's more than one candidate, let's go for variety
        self.current_state = random.choice(candidates)

        # These variables need to be cleared at the beginning of each run
        self.last_next_states = []
        self.next_state = None
        self.next_region = None

        # Bring our actuator states up-to-date
        for key, output_val in self.current_state.outputs.iteritems():
            # Skip any "bitX" region encodings
            if re.match('^bit\d+$', key): continue
            if key in self.actuators:
                new_val = output_val
                initial=False
                eval(self.actuator_handler[key])

        return self.current_state

    def runIteration(self):
        """
        Run, run, run the automaton!  (For one evaluation step)
        """

        # Let's try to transition
        next_states = self.findTransitionableStates()

        # Make sure we have somewhere to go
        if len(next_states) == 0:
            # Well darn!
            print "(FSA) ERROR: Could not find a suitable state to transition to!"
            return


        # See if we're beginning a new transition
        if next_states != self.last_next_states:
            # NOTE: The last_next_states comparison is also to make sure we don't
            # choose a different random next-state each time, in the case of multiple choices

            self.last_next_states = next_states

            # Only allow self-transitions if that is the only option!
            if len(next_states) > 1 and self.current_state in next_states:
                next_states.remove(self.current_state)

            self.next_state = random.choice(next_states)
            self.next_region = self.regionFromState(self.next_state)

            # See what we, as the system, need to do to get to this new state
            self.transition_contains_motion = self.next_region is not None and (self.next_region != self.current_region)

            if self.proj.compile_options['fastslow']:
                # Run actuators before motion
                self.updateOutputs(self.next_state)

            if self.transition_contains_motion:
                # We're going to a new region
                print "Heading to region %s..." % self.regions[self.next_region].name

            self.arrived = False


        if not self.arrived:
            # Move one step towards the next region (or stay in the same region)
            self.arrived = self.motion_handler.gotoRegion(self.current_region, self.next_region)

        # Check for completion of motion
        if self.arrived and self.next_state != self.current_state:
            # TODO: Check to see whether actually inside next region that we expected

            if self.transition_contains_motion:
                print "Crossed border from %s to %s!" % (self.regions[self.current_region].name, self.regions[self.next_region].name)

            if not self.proj.compile_options['fastslow']:
                # Run actuators after motion
                self.updateOutputs(self.next_state)

            self.current_state = self.next_state
            self.current_region = self.next_region
            self.last_next_states = []  # reset
            print "Now in state %s (z = %s)" % (self.current_state.name, self.current_state.rank)


         
if __name__ == "__main__":
    #### Test: Domains ####
    animals = ["cat", "dog", "red-backed fairywren", "pseudoscorpion", "midshipman"]
    d = Domain("favorite_animal", value_mapping=animals)
    print d
    assert d.num_props == 3
    for value in animals:
        p = d.valueToPropAssignments(value)
        print p
        assert value == d.propAssignmentsToValue(p)
    