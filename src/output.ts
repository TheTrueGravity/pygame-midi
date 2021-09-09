import {
    spawn,
    ChildProcessWithoutNullStreams
} from 'child_process'
import * as path from 'path'

export async function Send(id: number, data: [number, number, number], cooldown?: number) {
    let debug = false
    if (process.env.DEBUG == '1') {
        debug = true
    }
    
    if (debug) {
        console.log('python', [
            "-u",
            path.join(__dirname, "../python/output.py"),
            id.toString(),
            JSON.stringify(data)
        ])
    }

    spawn('python', [
        "-u",
        path.join(__dirname, "../python/output.py"),
        id.toString(),
        JSON.stringify(data)
    ])
    
    await new Promise(r => setTimeout(r, cooldown ? cooldown : 20))
}

export default class Output {
    private exec: ChildProcessWithoutNullStreams

    private enabled: boolean = false

    constructor(id: Number) {
        this.exec = spawn('python', [
            "-u",
            path.join(__dirname, "../python/output.py"),
            id.toString()
        ])

        this.exec.stdout.on('data', (data: String) => {
            // console.log(data.toString())
            if (data.toString().startsWith("Ready!")) { this.enabled = true }
        })
    }

    private async waitForReady() {
        if (!this.enabled) await new Promise(r => setTimeout(r, 20))
        if (!this.enabled) await this.waitForReady()
        // return this.enabled = false
    }

    public async sendMessage(message: number[]) {
        await this.waitForReady()
        this.exec.stdin.write(JSON.stringify(message) + "\n")
    }
}