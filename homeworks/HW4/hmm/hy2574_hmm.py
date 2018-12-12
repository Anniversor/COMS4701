import sys, math, random, copy

class HMM(object):
    # HMM model parameters #
    """
    Assume |X| state values and |E| emission values.
    initial: Initial belief probability distribution, list of size |X|
    tprob: Transition probabilities, size |X| list of size |X| lists;
           tprob[i][j] returns P(j|i), where i and j are states
    eprob: Emission probabilities, size |X| list of size |E| lists;
           eprob[i][j] returns P(j|i), where i is a state and j is an emission
    """
    def __init__(self, initial, tprob, eprob):
        self.initial = initial
        self.tprob = tprob
        self.eprob = eprob

    # Normalize a probability distribution
    def normalize(self, pdist):
        s = sum(pdist)
        for i in range(0,len(pdist)):
            pdist[i] = pdist[i] / s
        return pdist


    # Propagation (elapse time)
    """
    Input: Current belief distribution in the hidden state P(X_{t-1))
    Output: Updated belief distribution in the hidden state P(X_t)
    """
    def propagate(self, belief):
        new_beliefs = []
        for i in range(len(belief)):
            new_belief = 0
            for j in range(len(belief)):
                new_belief += self.tprob[j][i] * belief[j]
            new_beliefs.append(new_belief)
        belief = new_beliefs
        return belief

    # Observation (weight by evidence)
    """
    Input: Current belief distribution in the hidden state P(X_t),
           index corresponding to an observation e_t
    Output: Updated belief distribution in the hidden state P(X_t | e_t)  
    """
    def observe(self, belief, obs):
        for i in range(len(belief)):
            belief[i] = belief[i] * self.eprob[i][obs]

        belief = self.normalize(belief)
        return belief

    # Filtering
    """
    Input: List of t observations in the form of indices corresponding to emissions
    Output: Posterior belief distribution of the hidden state P(X_t | e_1, ..., e_t)
    """
    def filter(self, observations):
        belief = self.initial
        for obs in observations:
            belief = self.observe(self.propagate(belief), obs)
        return belief


    # Viterbi algorithm
    """
    Input: List of t observations in the form of indices corresponding to emissions
    Output: List of most likely sequence of state indices [X_1, ..., X_t]
    """
    def viterbi(self, observations):
        m = self.initial
        t_x = {}
        time_step = 0
        for obs in observations:
            time_step += 1
            m_new = []
            for i in range(len(m)):
                prop = []
                for j in range(len(m)):
                    prop.append(m[j]*self.tprob[j][i])
                max_prop = max(prop)
                m_new.append(self.eprob[i][obs] * max_prop)
                state_index = prop.index(max_prop)
                t_x[(time_step, i)] = state_index
            m = self.normalize(m_new)

        state = m.index(max(m))
        seq = []
        seq.append(state)
        for i in range(time_step,1,-1):
            state = t_x[(i, state)]
            seq.append(state)
        seq.reverse()

        return seq


# Functions for testing
# You should not change any of these functions
def load_model(filename):
    model = {}
    input = open(filename, 'r')
    i = input.readline()
    x = i.split()
    model['states'] = x[0].split(",")
    
    input.readline()
    i = input.readline()
    x = i.split()
    y = x[0].split(",")
    model['initial'] = [float(i) for i in y]

    input.readline()
    tprob = []
    for i in range(len(model['states'])):
        t = input.readline()
        x = t.split()
        y = x[0].split(",")
        tprob.append([float(i) for i in y])
    model['tprob'] = tprob

    input.readline()
    i = input.readline()
    x = i.split()
    y = x[0].split(",")
    model['emissions'] = dict(zip(y, range(len(y))))

    input.readline()
    eprob = []
    for i in range(len(model['states'])):
        e = input.readline()
        x = e.split()
        y = x[0].split(",")
        eprob.append([float(i) for i in y])
    model['eprob'] = eprob

    return model

def load_data(filename):
    input = open(filename, 'r')
    data = []
    for i in input.readlines():
        x = i.split()
        if x == [',']:
            y = [' ', ' ']
        else:
            y = x[0].split(",")
        data.append(y)
    observations = []
    classes = []
    for c, o in data:
        observations.append(o)
        classes.append(c)

    data = {'observations': observations, 'classes': classes}
    return data

def generate_model(filename, states, emissions, initial, tprob, eprob):
    f = open(filename,"w+")
    for i in range(len(states)):
        if i == len(states)-1:
            f.write(states[i]+'\n')
        else:
            f.write(states[i]+',')
    f.write('\n')

    for i in range(len(initial)):
        if i == len(initial)-1:
            f.write('%f\n'%initial[i])
        else:
            f.write('%f,'%initial[i])
    f.write('\n')

    for i in range(len(states)):
        for j in range(len(states)):
            if j == len(states)-1:
                f.write('%f\n'%tprob[i][j])
            else:
                f.write('%f,'%tprob[i][j])
    f.write('\n')

    for i in range(len(emissions)):
        if i == len(emissions)-1:
            f.write(emissions[i]+'\n')
        else:
            f.write(emissions[i]+',')
    f.write('\n')

    for i in range(len(states)):
        for j in range(len(emissions)):
            if j == len(emissions)-1:
                f.write('%f\n'%eprob[i][j])
            else:
                f.write('%f,'%eprob[i][j])
    f.close()


def accuracy(a,b):
    total = float(max(len(a),len(b)))
    c = 0
    for i in range(min(len(a),len(b))):
        if a[i] == b[i]:
            c = c + 1
    return c/total

def test_filtering(hmm, observations, index_to_state, emission_to_index):
    n_obs_short = 10
    obs_short = observations[0:n_obs_short]

    print('Short observation sequence:')
    print('   ', obs_short)
    obs_indices = [emission_to_index[o] for o in observations]
    obs_indices_short = obs_indices[0:n_obs_short]

    result_filter = hmm.filter(obs_indices_short)
    result_filter_full = hmm.filter(obs_indices)

    print('\nFiltering - distribution over most recent state given short data set:')
    for i in range(0, len(result_filter)):
        print('   ', index_to_state[i], '%1.3f' % result_filter[i])

    print('\nFiltering - distribution over most recent state given full data set:')
    for i in range(0, len(result_filter_full)):
        print('   ', index_to_state[i], '%1.3f' % result_filter_full[i])

def test_viterbi(hmm, observations, classes, index_to_state, emission_to_index):
    n_obs_short = 10
    obs_short = observations[0:n_obs_short]
    classes_short = classes[0:n_obs_short]
    obs_indices = [emission_to_index[o] for o in observations]
    obs_indices_short = obs_indices[0:n_obs_short]

    result_viterbi = hmm.viterbi(obs_indices_short)
    best_sequence = [index_to_state[i] for i in result_viterbi]
    result_viterbi_full = hmm.viterbi(obs_indices)
    best_sequence_full = [index_to_state[i] for i in result_viterbi_full]

    print('\nViterbi - predicted state sequence:\n   ', best_sequence)
    print('Viterbi - actual state sequence:\n   ', classes_short)
    print('The accuracy of your viterbi classifier on the short data set is', accuracy(classes_short, best_sequence))
    print('The accuracy of your viterbi classifier on the entire data set is', accuracy(classes, best_sequence_full))


# Train a new typo correction model on a set of training data (extra credit)
"""
Input: List of t observations in the form of string or other data type literals
Output: Dictionary of HMM quantities, including 'states', 'emissions', 'initial', 'tprob', and 'eprob' 
"""
def train(observations, classes):
    model = {
        'states': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', '_'],
        'emissions': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't',
                      'u', 'v', 'w', 'x', 'y', 'z', '_'],


    }
    model['initial'] = [0 for i in range(len(model['states']))]
    model['tprob'] = [[0 for j in range(len(model['states']))] for i in range(len(model['states']))]
    model['eprob'] = [[0 for j in range(len(model['states']))] for i in range(len(model['emissions']))]
    for i in range(len(observations)):
        time_now = model['states'].index(classes[i])
        if i < len(observations) - 1:
            time_next = model['states'].index(classes[i+1])
            model['tprob'][time_now][time_next] += 1
        evi_now = model['emissions'].index(observations[i])
        model['eprob'][evi_now][time_now] += 1

    for items in model['tprob']:
        n = sum(items)
        for i in range(len(items)):
            items[i] = items[i] / n

    for items in model['eprob']:
        n = sum(items)
        for i in range(len(items)):
            items[i] = items[i] / n

    initial_count = [0 for i in range(len(model['states']))]
    for i in range(len(classes)):
        initial_count[model['states'].index(classes[i])] += 1

    for i in range(len(model['states'])):
        model['initial'][i] = initial_count[i] / len(classes)

    for i in range(len(model['tprob'])):
        for j in range(len(model['tprob'][0])):
            if model['tprob'][i][j] == 0:
                model['tprob'][i][j] += 0.000001
            if model['eprob'][i][j] == 0:
                model['eprob'][i][j] += 0.000001
    return model

if __name__ == '__main__':
    # this if clause for extra credit training only
    if len(sys.argv) == 4 and sys.argv[1] == '-t':
        input = open(sys.argv[3], 'r')
        data = []
        for i in input.readlines():
            x = i.split()
            if x == [',']:
                y = [' ', ' ']
            else:
                y = x[0].split(",")
            data.append(y)

        observations = []
        classes = []
        for c, o in data:
            observations.append(o)
            classes.append(c)

        model = train(observations, classes)
        generate_model(sys.argv[2], model['states'], model['emissions'], model['initial'], model['tprob'], model['eprob'])
        exit(0)

    # main part of the assignment
    if len(sys.argv) != 3:
        print("\nusage: ./hmm.py [model file] [data file]")
        exit(0)

    model = load_model(sys.argv[1])
    data = load_data(sys.argv[2])

    new_hmm = HMM(model['initial'], model['tprob'], model['eprob'])
    test_filtering(new_hmm, data['observations'], model['states'], model['emissions'])
    test_viterbi(new_hmm, data['observations'], data['classes'], model['states'], model['emissions'])