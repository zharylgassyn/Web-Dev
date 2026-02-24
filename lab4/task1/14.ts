import {Component} from '@angular/core';
import { RouterLink,  RouterOutlet} from '@angular/router';

@Component({
  selector: 'app-root',
  template: `
    <nav>
      <a href="/">Home</a>
      |
      <a href="/user">User</a>
      <a routerLink="/">Home</a>
      <a routerLink="/user">User</a>
    </nav>
    <router-outlet />
  `,
  imports: [RouterLink, RouterOutlet],
})
export class App {}
