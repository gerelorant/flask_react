class AjaxComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {loaded: false};
    }

    componentDidMount() {
        this.getState();
    }

    getArgs() {
        return {}
    }

    get(url, params) {
        let args = "";
        Object.keys(params).forEach(function (k, i) {
            if (i === 0) {
                args += `?${k}=${params[k]}`;
            } else {
                args += `&${k}=${params[k]}`;
            }
        });
        return fetch(url + args);
    }

    getState() {
        this.setState({loaded: false});
        this.get(this.props.endpoint, this.getArgs()).then(function (response) {
            return response.json();
        }).then(function (response) {
            this.setState(response);
            this.setState({loaded: true});
        }.bind(this));
    }

    post(url, params) {
        return fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(params)
        });
    }

    postState() {
        let args = this.getArgs();
        args.update(this.state);
        this.setState({loaded: false});
        this.post(this.props.endpoint, args).then(function (response) {
            return response.json();
        }).then(function (response) {
            this.setState(response);
            this.setState({loaded: true});
        }.bind(this));
    }

    renderIfLoaded() {return ""}

    renderIfLoading() {return "Loading..."}

    render() {
        if( this.state.loaded ) {
            return this.renderIfLoaded()
        } else {
            return this.renderIfLoading()
        }
    }
}

class SocketComponent extends React.Component {
    constructor(props) {
        !('namespace' in props) && (props.namespace = '/');
        super(props);
        this.state = {
            loaded: false
        };
        this.socket = io(this.props.namespace);
        this.socket.on('state', function (data) {
            this.setState(data);
        }.bind(this));
    }

    requestState() {
        this.socket.emit('state_request');
    }

    emitState() {
        this.socket.emit('state', this.state);
    }
}