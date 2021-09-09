import {
    spawn, ChildProcessWithoutNullStreams
} from 'child_process'
import * as path from 'path'

export default class Input {
    private exec: ChildProcessWithoutNullStreams

    private onData: Function

    constructor(id: Number) {
        this.exec = spawn('python', [
            "-u",
            path.join(__dirname, "../python/input.py"),
            id.toString()
        ])

        this.onData = () => {}

        this.exec.stdout.on('data', data => {
            try {
                this.emit('data', JSON.parse(data))
            } catch {}
        })
    }

    private emit(type: 'data', data: any) {
        if (type == 'data') {
            this.onData(data)
        }
    }

    public on(type: 'data', func: Function) {
        if (type == 'data') {
            this.onData = func
        }
    }
}